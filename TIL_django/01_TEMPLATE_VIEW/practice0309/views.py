from django.shortcuts import render
from django.http.response import HttpResponse
import requests
import random
# Create your views here.

# 입력할 form&input html 제공
def ping(request):
    return render(request, 'practice0309/ping.html')

def pong(request):
    kr_name = request.GET.get('kor-name')
    en_name = request.GET.get('eng-name')
    fullname = kr_name + en_name
    context = {
        'fullname': fullname,
    }
    return render(request, 'practice0309/pong.html', context)


def var_route(request, value):
    return HttpResponse(value)



def lotto(request, value):
    # 1. 현실 로또 번호를 가져온다.
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={value}'
    lotto_dict = requests.get(url).json()
    real_data = {
        'numbers': [],
        'bonus_num': [],
        }
    for key in lotto_dict:
        if key.startswith('drwtNo'):
            real_data['numbers'].append(lotto_dict[key])
        elif key.startswith('bnusNo'):
            real_data['bonus_num'].append(lotto_dict[key])
    # real_data = {
    #     'numbers': [7, 9, 22, 27, 37, 42],
    #     'bonus_num': 34,
    # }

    numbers_1000 = [random.sample(range(1, 46), 6) for _ in range(1000)]
    first = second = third = fourth = fifth = gguang = 0
    for choice in numbers_1000:
        count = 0
        b_count = 0
        for number in choice:
            if number in real_data['numbers']:
                count += 1
            elif number in real_data['bonus_num']:
                b_count += 1
        if count == 6:
            first += 1
        elif count == 5 and b_count == 1:
            second += 1
        elif count == 5:
            third += 1
        elif count == 4:
            fourth += 1
        elif count == 3:
            fifth += 1
        else:
            gguang += 1
    context = {
        'numbers': real_data['numbers'],
        'bonus_num': real_data['bonus_num'],
        'first': first,
        'second': second,
        'third': third,
        'fourth': fourth,
        'fifth': fifth,
        'gguang': gguang,
    }


    return render(request, 'practice0309/lotto.html', context)


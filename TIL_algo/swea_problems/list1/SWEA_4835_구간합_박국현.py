T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_num, min_num = 0,0
    for number in numbers[:M]:
        max_num += number
        min_num += number

    idx = 0
    while idx + M < N + 1:
        summation = 0
        for number in numbers[idx: idx+M]:
            summation += number
        if summation > max_num:
            max_num = summation
        elif summation < min_num:
            min_num = summation
        idx += 1
    print('#{} {}'.format(test_case, max_num-min_num))
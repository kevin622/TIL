T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))
    count_list = [0] * 10

    for idx in range(N):
        count_list[cards[idx]] += 1

    max_card = 0
    max_count = 0
    for card, count in enumerate(count_list):
        if count >= max_count:
            max_count = count
            max_card = card
    print('#{} {} {}'.format(test_case, max_card, max_count))


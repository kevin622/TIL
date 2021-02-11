T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    D, L, N = map(int, input().split())
    damage = 0
    for n in range(N):
        damage += D * (1 + n * L * 0.01)
        # 이 식에 int를 바로 하면 어째서인지 오류남...파이썬 특징 때문에?


    damage = int(damage)
    print('#{} {}'.format(test_case, str(damage)))
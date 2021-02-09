T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    primes = [2, 3, 5, 7, 11]
    answer = [0] * 5
    idx = 0

    for prime in primes:
        while num % prime == 0:
            num //= prime
            answer[idx] += 1
        idx += 1
    print('#{} {} {} {} {} {}'.format(test_case, *answer))
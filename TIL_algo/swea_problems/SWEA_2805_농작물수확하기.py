def my_sum(l):
    answer = 0
    for i in l:
        answer += i
    return answer

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = []
    for _ in range(N):
        farm.append(list(map(int, input())))

    idx = 0
    start = N // 2
    end = N // 2 + 1
    answer = 0
    while idx < N:
        answer += my_sum(farm[idx][start: end])
        idx += 1
        if idx <= N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print('#{} {}'.format(test_case, answer))
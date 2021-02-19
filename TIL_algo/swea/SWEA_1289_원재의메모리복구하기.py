T = int(input())
for test_case in range(1, T + 1):
    org = list(map(int, input()))
    N = len(org)
    new = [0] * N

    count = 0
    for idx in range(N):
        if org[idx] != new[idx]:
            for j in range(idx, N):
                new[j] = org[idx]
            count += 1
    print('#{} {}'.format(test_case, count))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, Q = list(map(int, input().split()))
    boxes = ['0'] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for idx in range(L-1, R):
            boxes[idx] = str(i)
    answer = ' '.join(boxes)
    print('#{} {}'.format(test_case, answer))
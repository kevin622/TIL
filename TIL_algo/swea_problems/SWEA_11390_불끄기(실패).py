T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    room_count = 0
    floor_count = 0
    for i in range(N):
        matrix.append(list(input()))
        on_count += matrix[-1].count('#')
        if '#' in matrix[-1]:
            floor_count += 1

    answer = 0
    floor = 0
    room = 0
    if room_count != 0:
        while True:
            # 현재 층에 불 켜진 곳 확인
            if '#' in matrix[floor]:
                for _ in range(M):
                    room += 1
                    answer += 1
                    if matrix[floor][room] == '#':
                        matrix[floor][room] == '.'
                        answer += 1
                        if '#' not in matrix[floor]:
                            floor_count -= 1
                            break

            if floor_count == 0:
                break

            # 다음 불 켜진 층 찾기
            for next_idx in range(floor+1, N):
                if '#' in matrix[next_idx]:
                    new_floor = matrix[next_idx]
                    # 가장 왼쪽에 있는 불켜진 방
                    for idx in range(M):
                        if new_floor[idx] == '#':
                            left = idx
                            break
                    for idx in range(M-1, -1, -1):
                        if new_floor[idx] == '#':
                            right = (M-1) - idx
                            break

                    if left >




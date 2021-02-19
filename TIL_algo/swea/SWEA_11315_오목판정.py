T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(input())

    answer = 'NO'
    for row_idx in range(N):
        # 가로 행 확인
        if 'ooooo' in matrix[row_idx]:
            answer = 'YES'
            break

        # 세로 열 확인
        if row_idx + 4 < N:
            for col_idx in range(N):
                if ''.join([matrix[row_idx + i][col_idx] for i in range(5)]) == 'ooooo':
                    answer = 'YES'
                    break

                # 대각선 확인
                if col_idx + 4 < N:
                    if ''.join([matrix[row_idx + i][col_idx + i] for i in range(5)]) == 'ooooo':
                        answer = 'YES'
                        break
                if col_idx - 4 >= 0:
                    if ''.join([matrix[row_idx + i][col_idx - i] for i in range(5)]) == 'ooooo':
                        answer = 'YES'
                        break

        if answer == 'YES':
            break

    print('#{} {}'.format(test_case, answer))
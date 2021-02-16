def turn_clockwise(square):
    return [[square[row][col] for row in range(len(square)-1, -1, -1)]
            for col in range(len(square))]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    matrix_90 = turn_clockwise(matrix)
    matrix_180 = turn_clockwise(matrix_90)
    matrix_270 = turn_clockwise(matrix_180)

    print('#{}'.format(test_case))
    for i in range(N):
        print(''.join(map(str, matrix_90[i])), end=' ')
        print(''.join(map(str, matrix_180[i])), end=' ')
        print(''.join(map(str, matrix_270[i])))

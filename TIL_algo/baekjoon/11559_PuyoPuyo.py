def DFS(start, connections):
    stack = [start]
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if v in connections:
                for w in connections[v]:
                    stack.append(w)
    return visited


def get_connections(matrix):
    connections = {}
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for r in range(12):
        for c in range(6):
            if matrix[r][c] != '.':
                for i in range(4):
                    if 0 <= r + dy[i] < 12 and 0 <= c + dx[i] < 6:
                        if matrix[r][c] == matrix[r + dy[i]][c + dx[i]]:
                            connections[(r, c)] = connections.get((r, c), []) + [(r + dy[i], c + dx[i])]
    return connections

matrix = []
for _ in range(12):
    matrix.append(list(input()))

answer = 0
while True:
    connections = get_connections(matrix)
    if not connections:
        break
    combo_points = []
    for r in range(12):
        for c in range(6):
            if matrix[r][c] != '.' and (r, c) not in combo_points:
                combo = DFS((r, c), connections)
                if len(combo) >= 4:
                    combo_points.extend(combo)
    if not combo_points:
        break
    for r, c in combo_points:
        matrix[r][c] = '.'

    for r in range(11, 0, -1):
        for c in range(6):
            if matrix[r][c] == '.':
                bottom_idx = r
                for r2 in range(r - 1, -1, -1):
                    if matrix[r2][c] != '.':
                        matrix[r][c] = matrix[r2][c]
                        matrix[r2][c] = '.'
                        break
    answer += 1
print(answer)
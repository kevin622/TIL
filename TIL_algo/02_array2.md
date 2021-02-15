# 배열 Array 2

## 2차원 배열

- (보통 다수의)1차원 리스트를 원소로 갖는 리스트
- 다수의 인덱스를 사용해야 개별 원소에 접근 가능

### 배열 순회

`n X m`  배열의 n * m 개의 원소에 모두 접근(조사)하는 것

```python
array = [[1, 2, 3], [4, 5, 6], ...] # 2차원 리스트
N = len(array)
M = len(array[0])
```

- 행 우선 순회

```python
for row_idx in range(N):
  for col_idx in range(M):
    array[row_idx][col_idx]
```

- 열 우선 순회

```python
for col_idx in range(M):
  for row_idx in range(N):
    array[row_idx][col_idx]
```

- 지그재그 순회

```python
for row_idx in range(N):
  for col_idx in range(M):
    array[row_idx][col_idx + (col_idx%2)*(M-1 - col_idx*2)]
```

- **델타** 를 이용한 2차원 배열 탐색

```python
# 상하좌우 순
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for row_idx in range(N):
  for col_idx in range(M):
    for mode in range(4):
      array[row_idx + dx[mode]][col_idx + dy[mode]]
```

- 전치 행렬

```python
# 정사각행렬이라는 가정 하에
for row_idx in range(N):
  for col_idx in range(N):
    if row_idx > col_idx:
      array[row_idx][col_idx], array[col_idx][row_idx] = array[col_idx][row_idx], array[row_idx][col_idx]
```


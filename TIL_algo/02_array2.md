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



## 부분집합

완전탐색의 방법으로 모든 부분집합 추출 방법

### 비트 연산자

- `&` : 비트 단위의 and 연산

- `|` : 비트 단위의 or 연산

- `<<` : 피연산자의 비트 열을 왼쪽으로 이동

  - $$
    1 << n => 2^n
    $$

    즉 원소가 n개인 집합의 모든 부분집합의 수

- `>>`  : 피연산자의 비트열을 오른쪽으로 이동

```python
i & (1 << j)
```

i의 j 번째 비트가 1인지 확인(해당 비트값이 1이고 나머지는 0인 십진수를 반환)

### 비트 연산자로 부분집합 구하기

```python
arr = [1, 2, 3]
n = len(arr)

for i in range(1 << n):  # 부분집합 수만큼 for 실행
    subset = []
    for j in range(n):  # 원소의 수만큼 비트 비
        if i & (1 << j):  # i의 j번째 비트가 1이면 arr 의 j번째 원소 append
            subset.append(arr[j])
    print(subset)
```

```
[]
[1]
[2]
[1, 2]
[3]
[1, 3]
[2, 3]
[1, 2, 3]
```

공집합도 포함되니 확인할 것!

## 검색 Search

저장되어 있는 자료 중 원하는 항목을 찾는 작업

- 순차 검색 Sequential Search
- 이진 검색 Binary Search
- 해쉬 Hash

### 순차 검색

순서대로 검색하는 방법

- 정렬되어 있지 않은 경우 : 끝까지 찾았는데 없으면 검색 실패

$$
O(n)
$$

- 정렬되어 있는 경우 : 찾다가 원소의 값이 찾고자 하는 키값보다 커지면 검색 실패
  - 정렬되어 있으므로 검색 실패 반환하는 경우 평균 비교 횟수가 반으로 줄어들지만..

$$
O(n)
$$

시간 복잡도 기준으로 둘 다 비슷!

### 이진 검색

연속적으로 가운데를 비교하며 검색 범위를 줄이는 방법

_반드시! 자료는 **정렬** 되어있어야 함_

```python
def binary_search(list_obj, k):
    start = 0
    end = len(list_obj) - 1
    while start <= end:
        middle = (start + end) // 2
        if list_obj[middle] == k:
            return True
        elif list_obj[middle] > k:
            end = middle - 1
        elif list_obj[middle] < k:
            start = middle + 1
    return false
```


# 스택 Stack 2

## 계산기

**후위표기법** : 연산자를 피연산자 뒤에 표기하는 방법, stack 을 이용. 중위표기법으로 표현된 수식을 앞부터 읽어나가며

1. 토큰이 피연산자(숫자)이면 출력
2. 토큰이 연산자(왼쪽괄호 포함)이면, 더 낮은 우선순위의 연산자가 나올 때까지 stack 에서 pop 한 것을 출력, 더 낮은 우선순위의 연산자가 나오거나 stack 이 비어있으면 push
3. 토큰이 오른쪽 괄호일 경우 왼쪽 괄호가 나올 때까지 stack 에서 pop 한 것을 출력, 오른쪽 괄호가 나올 경우 출력 없이 그냥 pop
4. 읽을 것이 없을 때까지 반복
5. 읽을 것이 없는데 stack 이 비어있지 않다면 순서대로 pop 하며 출력

```
icp(in-coming priority)
isp(is-stack priority)

if (icp > isp) push()
else pop()
```

| token | isp  | icp  |
| ----- | ---- | ---- |
| )     | -    | -    |
| *, /  | 2    | 2    |
| +, -  | 1    | 1    |
| (     | 0    | 3    |

**후위표기법 계산** : 스택 이용, 후위표기법으로 표현된 수식을 읽어내려가며

1. 토큰이 피연산자이면(숫자면) push
2. 토큰이 연산자이면 stack에서 pop 두 번, 순서를 지켜서 연산을 한 결과를 다시 push
3. 수식을 다 읽었으면 pop(하나의 원소만 stack에 남아있을 것이므로)



## 백트래킹 Backtracking

해를 찾는 중 유망하지 않으면 (해가 될 가능성이 0이면) 끝까지 확인하지 않고 다시 되돌아가서 해를 찾는 알고리즘, **최적화 / 결정** 문제에 이용

- 미로 찾기
- N-Queen
- Map Coloring
- 부분집합의 합

> 진행 절차

1. 깊이 우선 탐색 실행
2. 각 노드가 유망한지 점검
3. 유망하지 않다면 부모 노드로 돌아가서 검색을 계속함



### 순열

```python
def perm_back(idx):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                perm_back(idx + 1)
                check[i] = 0
```

```python
def perm_swap(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm_swap(idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx]
```

```python
def perm_bit(idx, check):
    if idx == N:
        print(sel)
    else:
        for j in range(N):
            if check & (1 << j):
                continue
            else:
                sel[idx] = arr[j]
                perm_bit(idx + 1, check | (1 << j))
```



## 분할 정복 알고리즘

- 거듭제곱

```python
def power(base, exp):
    if base == 0 or exp == 0:
        return 1
    elif exp % 2 == 0:
        new_base = power(base, exp // 2)
        return new_base * new_base
    else:
        new_base = power(base, exp // 2)
        return new_base * new_base * base
```

문제를 작은 두 문제로 나눌 수 있다면 시도! 재귀가 깊지 않고 시간 복잡도는 **O(logn) **

## 퀵 정렬

기준 아이템(pivot)을 중심으로 작은 것을 왼편, 큰 것을 오른편에 위치시킴

```python
def quick_sort(array, begin, end):
    if begin < end:
        P = partition(array, begin, end)
        quick_sort(array, begin, P-1)
        quick_sort(array, P+1, end)

def partition(array, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while array[L] < array[pivot] and L < R:
            L += 1
        while array[R] >= array[pivot] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            array[L], array[R] = array[R], array[L]
    array[pivot], array[R] = array[R], array[pivot]
    return R
```

최악의 경우 O(n^2)의 시간복잡도를 가지지만, 평균적으로 nlogn임

> 참고 : 지금까지 살펴본 정렬 방법론 정리

| 알고리즘    | 평균수행시간 | 최악수행시간 | 알고리즘 기법 | 비고                             |
| ----------- | ------------ | ------------ | ------------- | -------------------------------- |
| 버블 정렬   | O(n^2)       | O(n^2)       | 비교와 교환   | 코딩이 가장 쉬운 편              |
| 카운팅 정렬 | O(n + k)     | O(n + k)     | 비교환        | n이 비교적 작을 때 가능          |
| 선택 정렬   | O(n^2)       | O(n^2)       | 비교와 교환   | 교환의 횟수가 버블 정렬보다 적음 |
| 퀵 정렬     | O(nlogn)     | O(n^2)       | 분할 정복     | 평균적으로 가장 빠름             |


# 배열 Array 1 

배열이란?

- 일정한 자료형의 변수들을 따로 사용하지 않고 하나의 이름으로 열거하는 자료 구조

- 다수의 변수를 사용하기 힘들 때, 또는 다수의 변수를 만드는 것이 효율적이지 않은 경우 사용

## 완전 검색(완전 탐색) Exhaustive Search

- 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열하고 확인
- 동의어: Brute-force, Generate-and-test

- 느리지만, 해를 못 찾을 확률은 작음

> 참고 : 순열

$$
nPr = n * (n-1) * ... * (n-r+2) * (n-r+1)
$$



## 탐욕 알고리즘 Greedy Algorithm

- 최적해를 찾는 근시안적 방법
- 해를 찾는 과정에서 그 **순간** 에 최적인 해를 선택
- 지역적(local)으로는 최적인 해가 전체(global) 최적은 아닐 수 있음!
  - 일반적으로 머리에서 떠오르는대로 검증 없이 구현하면 탐욕 알고리즘인 경우가 많음



### 동작 과정

1. 해 선택 : 지역적 최적해를 구하고 부분해 집합(Solution Set)에 추가
2. 실행 가능성 검사 : 실행 가능한지, 제약 조건을 위배하지 않는지 검사
3. 해 검사 : 부분해 집합이 전체 해가 맞는지 확인하고, 아직 아니라면 1번부터 반복



## 정렬

- 정렬이란?

2개 이상의 자료를 특정 기준에 의해 오름차순(ascending)이나 내림차순(descending)으로 재배열하는 것

- 키

자료를 정렬하는 기준이 되는 특정 값



> 참고 : 정렬의 종류

- 버블 정렬 Bubble Sort
- 카운팅 정렬 Counting Sort
- 선택 정렬 Selection Sort
- 퀵 정렬 Quick Sort
- 삽입 정렬 Insertion Sort
- 병합 정렬 Merge Sort



## 버블 정렬 Bubble Sort

- 인접한 두 원소를 비교해 큰 값을 뒤로 뒤로, 작은 값을 앞으로 위치시켜 정렬하는 방법

- 한 단계가 끝나면 가장 큰 수가 가장 뒤로 감
  $$
  O(n^2)
  $$

```python
def Bubble_sort(list_object):
  for idx in range(len(list_object)-1, 0, -1):
    for j in range(0, idx):
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
```




# 스택 Stack 1

- 스택에 저장된 자료는 선형 구조를 가짐
  - 선형구조 : 자료 간의 관계가 1:1
  - 비선형구조 : 자료 간의 관계가 1:N
- 후입선출 : **LIFO** Last In First Out
- C 언어에서는 크기를 정한 배열을 이용함, 마지막 삽입된 원소의 위치를 top 이라고 함

> 참고: 괄호검사는 스택을 써서 쉽게 해결 가능!

> 참고2: 함수 호출(재귀를 떠올리자)은 시스템 스택에 함수 실행 정보가 쌓이고 삭제되는 과정임

## Memoization

- 재귀 함수의 중복 호출 문제를 해결할 수 있는 방법, 이전에 계산된 값을 메모리에 저장시킴
- 중복 호출 때마다 다시 계산하지 않고 이미 저장된 값을 사용

피보나치에 적용 => 계산된 값들을 리스트에 저장

```python
memo = [0, 1]
def fibo_memo(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo_memo(n-1) + fibo_memo(n-2))
    return memo[n]
```

## 동적 계획법 Dynamic Programming

- 최적화 문제 해결 알고리즘
- 입력 크기가 작은 문제들을 해결한 후 그 해를 이용해 큰 문제 해결

피보나치에 적용 => fibo(n)은 결국 fibo(n-1), ... , fibo(0)의 부분집합으로 나뉨

```python
def fibo_dp(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    return f[n]
```


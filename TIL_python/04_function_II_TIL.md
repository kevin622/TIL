# 함수(function) II

- 이전에는 몰랐던, 혹은 헷갈렸던 내용 위주로 정리함
- 싸피의 `ipynb` 파일 내용을 다시 정리함

## 함수와 스코프(scope)

`scope` : 코드 내부의 공간. 함수로 생성된 공간은 지역 스코프이며, 그 이외에는 전역 스코프이다. (`enclosed scope` 도 있지만 그렇게 중요하지는 않다)

- **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
- **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간

- **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
- **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수



### 이름 검색 규칙

**`LEGB Rule`** : 파이썬의 절대원칙 중 하나. 파이썬이 다양한 이름공간(`name space`)에서 이름을 찾아나가는 순서.

- `L`ocal scope

- `E`nclosed scope : 함수 내에서 새로운 함수가 정의되었을 때 따진다.

- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈, 코드 내애서의 스코프

- `B`uilt-in scope: 파이썬 내장

```python
print('hello universe')  # 실행된다
print = 'new_name'  # local scope에 이름 생성
print('bye universe')  # TypeError

del print  # local scope에서 이름 삭제
print("I'm back!")  # 다시 된다!

del print  # Built-in scope에서 이름 삭제
print('Bye...')  # NameError
```

### 변수의 수명 주기

식별자에는 `수명주기(lifecycle)`가 있음

- **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지

- **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날때 까지 유지, 파이썬 코드가 종료되면 없어짐

- **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨), 즉 `return` 이후 없어짐

## 재귀함수(Recursive Function)

> 프로그래밍 3대장 : 재귀함수, 포인터, OOP(클래스)

내부에서 자기 자신을 호출하는 함수

```python
def sum_recur(N):
    if N == 1:
        return 1
    else:
        return N + sum_recur(N-1)
```

- 범위가 줄어드는 문제에 적합
- 범위가 더 이상 줄어들지 않는 최종적으로 `base case` 존재해야 함
- 코드가 직관적이고 알기 쉬운 경우가 많음 
- 변수 사용을 줄일 수 있음
- 함수가 호출될 때마다 메모리 공간에 쌓여 메모리 스택이 넘치거나(Stack Overflow) 프로그램 실행 속도가 느려질 수 있음

### 최대재귀깊이

위의 문제를 방지하기 위해 파이썬은 재귀가 1000번이 넘어가면 더이상 함수를 호출하지 않는데, 이를 최대 재귀 깊이(Maximum Recursion Depth)라 함

```python
def ssafy():
    print('', end = '')
    ssafy()

ssafy()
# RecursionError: maximum recursion depth exceeded while calling a Python object
```


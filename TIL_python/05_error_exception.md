# 에러 / 예외처리

시험엔 안 나온단다^^7

## 에러 종류

### 문법 에러 Syntax Error

> 실행 자체가 되지 않는다!

```python
if True print('참')
# SyntaxError: invalid syntax

print('Hi)
# SyntaxError: EOL while scanning string literal
# EOL - 따옴포 에러
      
print('Hi'
# SyntaxError: unexpected EOF while parsing
# EOf - 괄호닫기 에러
```



### 예외 Exception

> 예상하지 못한 상황(Exception)을 맞이하면 프로그램이 멈춤

```python
10 * (1/0)
# ZeroDivisionError: division by zero

print(abc)
# NameError: name 'abc' is not defined

1 + '1'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 자료형에 대한 에러
```



#### 함수 호출 과정 에러

```python
round('3.5')
# TypeError: type str doesn't define __round__ method

import random
random.sample([1, 2, 3])
# TypeError: sample() missing 1 required positional argument: 'k'

random.choice([1, 2, 3], 6)
# TypeError: choice() takes 2 positional arguments but 3 were given
```

#### 그 외 특이 에러

```python
int('3.5')
# ValueError: invalid literal for int() with base 10: '3.5'

numbers = [1, 2]
numbers.index(3)
# ValueError: 3 is not in list

empty_list = []
empty_list[1]
# IndexError: list index out of range

songs = {'sia': 'candy cane lane'}
songs['queen']
# KeyError: 'queen'

import reque
# ModuleNotFoundError: No module named 'reque'

from random import sampl
# ImportError: cannot import name 'sampl' from 'random'

# 사용자가 의도적으로 멈췄을 때
# 노트북의 정지 버튼과 같은 경우!
while True:
    continue
# KeyboardInterrupt: 
```



## 예외 처리

기본 문법

```python
try:
  <코드 블럭1>
except (Exception): 
  <코드 블럭2>
```

### as

```python
try:
    empty_list = []
    print(empty_list[-1])
except IndexError as err:
    print(f'{err}, 오류가 발생했습니다.')
# list index out of range, 오류가 발생했습니다.
```

인덱스 에러라는 말이 출력이 안 되고, 에러 상세내용만 출력됨



### 복수의 예외

```python
try:
    num = input('100으로 나눌 값을 입력하시오 : ')
    print(100/int(num))
except (ValueError, ZeroDivisionError):
    print('나눌 수 있는 걸 줘')
```

```python
try:
    num = input('100으로 나눌 값을 입력하시오 : ')
    print(100/int(num))
except ValueError:
    print('숫자를 써')
except ZeroDivisionError:
    print('0 말고')
```

이 경우 순차적으로 코드가 진행되므로, 작은 범주부터 시작해야 함.

즉 모든 에러를 다 따지고 싶은 그냥 `except`는 제일 마지막에 쓸 것.

### else

`try` 구문이 잘 실행되었을 때 실행할 구문

```python
try:
    num = input('100으로 나눌 값을 입력하시오 : ')
    print(100/int(num))
except (ValueError, ZeroDivisionError):
    print('나눌 수 있는 걸 줘')
else:
    print('잘했어!')
```

### finally

예외에 상관없이 실행되어야 할 코드

```python
try:
    num = input('100으로 나눌 값을 입력하시오 : ')
    print(100/int(num))
except (ValueError, ZeroDivisionError):
    print('나눌 수 있는 걸 줘')
else:
    print('잘했어!')
finally:
  	print('프로그램 종료')
```

### raise 와 assert

- `raise` : 예외를 강제로 발생시킴, 커스텀 에러 메시지를 보여주기 위해 사용

```python
class NoTestError(ZeroDivisionError):
    pass

raise NoTestError ('저런')
# NoTestError: 저런
```

- `assert` : 상태를 검증할 때 사용, 무조건 `AssertionError` 발생

```python
a = 1000
b = 1000
assert a is b, '주소값이 다릅니다.'
# AssertionError: 주소값이 다릅니다.
```


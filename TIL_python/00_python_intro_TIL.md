# Python 기초

- 이전에는 몰랐던, 혹은 헷갈렸던 내용 위주로 정리함
- 싸피의 `ipynb` 파일 내용을 다시 정리함

## 주석

여러 줄 주석을 위해 `'''` 를 사용하기도 함.

즉 `string` 을 만들되 할당하지 않음으로 주석의 역할을 하게 함

```python
'''
여기는 주석
두 줄도 가능
'''
print('여기는 코드 라인')
```

## 리스트의 특이한 convention

리스트 등에 여러 줄이 들어갈 경우 마지막 원소에도 `,` 를 넣는 것이 관례이다.

```{python}
lunch_menus = [
    '짜장면', 
    '짬뽕', 
    '탕수육', 
    '군만두', 
    '물만두', 
    '왕만두',  # 리스트의 마지막은 콤마(,)로 끝내는 습관 들이기!!!
]

print(lunch_menus)
```



## 변수

### 변수 바꾸기(스와핑)

파이썬만 가능한 방법

```{python}
x = 1
y = 2
x, y = y, x
```

모든 언어에서 가능한 방법

```{python}
x = 1
y = 2
x = x + y
y = x - y
x = x - y
```



### 식별자(변수명)

키워드

```{python}
import keyword
print(keyword.kwlist)
```
```
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

**내장함수 이름이나 모듈명 등도 조심행 함!**



## 숫자(Number) 타입

**파이썬에서 표현할 수 있는 가장 큰 수**

파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형(**integer**)에서 오버플로우(**overflow**)가 없다.임의 정밀도 산술(**arbitrary-precision arithmetic**)을 사용하기 때문이다. 

> **오버플로우(overflow)**
- 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있다.
- 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리가 차고 넘쳐 흐르는 현상

> **임의 정밀도 산술(arbitrary-precision arithmetic)**
- 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태
- 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용할 수 있게 유동적으로 운용

### n진수

```{python}
binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hexadecimal_number = 0x10  # 색표현, C의 메모리 주소값 표현 등 컴퓨터 세상에 많이 쓰임
print(f"""
2진수 : {binary_number}
8진수 : {octal_number}
10진수 : {decimal_number}
16진수 : {hexadecimal_number}
""")
```

```
2진수 : 2
8진수 : 8
10진수 : 10
16진수 : 16
```

### 실수 연산

```{python}
3.5 - 3.12
```

```
0.3799999999999999
```

따라서 다른 방법으로 `==` 을 확인해야 함

```{python}
a = 3.5 - 3.12
b = 0.38 

# 1번 방법
abs(a-b) <= 1e-10

# 2번 방법
import sys
abs(a-b) <= sys.float_info.epsilon

# 3번 방법
import math
math.isclose(a,b)
```

### 복소수

```{python}
complex('1 + 2j') # ValueError
```

## 문자 타입

### 이스퀘이프 시퀀스

| 예약문자 |    내용(의미)     |
| :------: | :---------------: |
|    \n    |      줄 바꿈      |
|    \t    |        탭         |
|    \r    |    캐리지리턴     |
|    \0    |     널(Null)      |
|   \\\\   |        `\`        |
|   \\'    | 단일인용부호(`'`) |
|   \\"    | 이중인용부호(`"`) |

### String Interpolation

잘 안 쓰기는 하지만, `%` 를 사용해서 포맷팅을 할 수 있음

- `%-formatting`

```python
name = 'Kim'
score = 4.5

print('Hello, %s' % name)
print('내 성적은 %d' % score)
print('내 성적은 %f' % score)
```

`f-string` 의 경우 연산과 출력형식 지정도 가능

- `f-string` 

```python
import datetime
today = datetime.datetime.now()
f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'
```

```
> 오늘은 21년 01월 20일 Wednesday
```

## 참/거짓(Boolean) 타입

### False 로 나오는 경우

- int `0`
- float `0.0`
- tuple `()`
- list `[]`
- dictionary `{}`
- string `''`
- boolean `False`
- `None`



### 단축평가

- 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않음
- 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상

```python
'a' and 'b' and '' and 'c'
```

```
>>> ''
```

```python
'' or '' or False or 0 or 'a' or 'b'
```

```
>>> 'a'
```



## Identity 연산자

`is` : 동일한 object인지 확인할 수 있음

- 파이썬에서 -5 부터 256 까지의 id는 동일함
- 의도적으로 공백없는 알파벳 문자열도 같게끔 해놓음
  - 단, 느낌표 등 특수문자가 섞인 `string` 은 같지 않음



## 연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 `**`
5. 단항연산자 `+`, `-` (음수/양수 부호)
6. 산술연산자 `*`, `/`, `%`
7. 산술연산자 `+`, `-`
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`



## 문장(statement)과 표현식(expression)

<center><img width="600" height="300" src="https://user-images.githubusercontent.com/9452521/87619771-f41f5e00-c757-11ea-9e4b-1f76e4ca0981.png", alt="variable"/></center>


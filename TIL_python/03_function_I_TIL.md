# 함수(function) I

- 이전에는 몰랐던, 혹은 헷갈렸던 내용 위주로 정리함
- 싸피의 `ipynb` 파일 내용을 다시 정리함

-----------

들어가기에 앞서...

1. 함수는 하나의 **'값'**이다. (로직 덩어리)
2. 변수와 똑같이 **'박스'**이다.

> 정의 : 특정한 기능(function)을 하는 코드의 묶음



## 내장함수

파이썬 내장함수 목록 확인 => `dir`를 이용해 가능하다

```python
dir(__builtin__)
```



## 반환값이 없는 경우

아무것도 리턴하지 않는 함수(정의에 `return`이 없는 함수)는 `None`을 리턴하는 것과 같다

```python
hello = print('hello')
print(hello, type(hello))
```

```
hello
None <class 'NoneType'>
```



## 매개변수(Parameter)와 전달인자(Argument)

(1) 매개변수 Parameter

- 입력을 받아 함수 내부에서 활용할 **변수**
- 함수의 **정의**에서 볼 수 있음

(2) 전달인자 Agrument

- 실제로 전달되는 **입력값**
- 함수의 **호출**에서 볼 수 있음

### 위치인자(Positional Argument)

함수는 기본적으로 위치를 통해 인자 판단

```python
import math
def cylinder(r, h):
    return math.pi * (r**2) * h
  
print(cylinder(5,2))
print(cylinder(2,5))
```

```
157.07963267948966
62.83185307179586
```



### 기본인자

기본 인자 뒤에 기본이 아닌 인자가 따라오면 안 됨

```python
def greeting(name='익명', age):
    print(f'{name}, 안녕? 난 {age}살이야.')
# SyntaxError: non-default argument follows default argument
```

정의조차 되지 않는다.

또한 정의가 잘 되었다 해도, 키워드 인자를 활용한 다음에 기본 인자를 활용할 경우 호출에서 에러가 남

```python
def greeting(age, name='익명'):
    print(f'{name}, 안녕? 난 {age}살이야.')

greeting(age=100, '국현')
# SyntaxError: positional argument follows keyword argument
```

## 가변 인자

### 가변 인자 리스트

개수가 정해지지 않은 임의의 인자를 받기 위해서는 `*args`를 활용

`tuple` 형태로 처리가 됨

```python
def hello(*names):
    for name in names:
        print(f'Hello, {name}.')
```

### 가변 키워드 인자

개수가 정해지지 않은 키워드 인자는 **`dict`** 형태로 처리가 되며, `**kwargs`로 표현

```python
def my_url(**kwargs):
    url = 'https://api.go.kr?'
    for key, value in kwargs.items():
        url+= f'{key}={value}&'
    return url
  
print(my_url(sidoname='서울', key='asdf'))
```

```
https://api.go.kr?sidoname=서울&key=asdf&
```




# 데이터 구조 (Data Structure) I

데이터에 편리하게 접근하고 변경하기 위해 데이터를 조작하거나 저장하는 방법

## 문자열

-  `Immutable`
- `Ordered` (== `Sequential`)
- `Iterable`

### `.find(x)`와 `.index(x)`

- find: x의 첫 위치, 없으면 -1을 반환
- index: x의 첫 위치, 없으면 에러(ValueError), 리스트에

### `.replace(old, new, count=-1)`

count를 지정하면 지정한 숫자만큼 앞부터 교체한 결과를 반환

### 문자변형

- `.capitalize()`
- `.title()`
- `.upper()`
- `.lower()`
- `.swapcase()`

### 검증 메서드

```python
.isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower()
```

`.isdecimal(), .isdigit(), .isnumeric()` 세 메서드는 기본적으로 비슷하고, 특정 유니코드에 대해 다르게 동작.

`isnumeric()` 이 가장 많은 경우를 포괄함(?)



## 리스트

### `.extend(iterable)`

iterable하면 다 추가 가능! string을 넣을 경우 리스트로 바뀌어 추가된다.

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.extend('ediya')
print(cafe)
# ['starbucks', 'tomntoms', 'hollys', 'e', 'd', 'i', 'y', 'a']
```

### `.remove(x)`

리스트에서 처음 나오는 x를 삭제

```python
numbers = [1, 2, 3, 1, 2]
numbers.remove(1)
print(numbers)
# [2, 3, 1, 2]
```

리스트에 없는 값을 넣을 경우 ValueError

### `.clear()`

리스트의 모든 항목을 제거하고 빈 리스트로 만듦

```python
a = [1, 2, 3]
a.clear()
print(a)
# []
```

### `.index()`

없는 값을 찾으면 ValueError!

### `.reverse()`

반대로 뒤집기

```python
classroom = ['Tom', 'David', 'Justin']
classroom.reverse()
print(classroom)
# ['Justin', 'David', 'Tom']
```

## 데이터의 분류

### immutable

- `literal` : `string`, `number`, `bool`

- `range`
- `tuple`

같은 값이라면 모든 변수가 같은 주소값을 참조하기 때문에 변경이 가능하면 안 된다!

```python
num1 = 10
num2 = 10
num1 is num2
# True
```

### mutable

- `list`, `set`, `dict`

같은 값을 생성하더라도 다른 주소값에 저장됨. 각자의 주소값이 다르기 때문에 데이터가 변하는 것이 큰 문제가 되지 않음

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1 is list2
# False
```

## 리스트의 복사 방법

```python
list1 = [1, 2, 3]
list2 = list1
list1[0] = 100
print(list2)
# [100, 2, 3]
```

위와 같이 복사할 경우 원래 변수의 데이터를 바꿀 경우 다음 변수의 데이터도 바뀐다.

리스트의 값만 복사하는 방법은?

### 얕은 복사 (shallow copy)

- `slicing`

```python
list1 = [1, 2, 3]
list2 = list1[:]
list1[0] = 100
print(list2)
# [1, 2, 3]
```

- `list()`

```python
list1 = [1, 2, 3]
list2 = list(list1)
list1[0] = 100
print(list2)
# [1, 2, 3]
```

하지만 위와 같은 방법들의 경우, 중첩된 리스트는 또 같은 주소값을 참조한다;;;;;

### 깊은 복사 (deep copy)

```python
import copy
a = [[1, 2, 3], 2, 3]
b = copy.deepcopy(a)
b[0][0] = 100
b[1] = 'new'
print(a, b)
# [[1, 2, 3], 2, 3] [[100, 2, 3], 'new', 3]
```



> 참고 : `map`, `filter`, `zip` 은 모두 인자로`iterable` 한 객체를 받는다!


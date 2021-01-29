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


# 컨테이너 (Container)

- 이전에는 몰랐던, 혹은 헷갈렸던 내용 위주로 정리함
- 싸피의 `ipynb` 파일 내용을 다시 정리함



## Sequence Container

- index 접근 가능하면 순서가 있는 시퀀스다!
- 종류 : `list` , `tuple` , `range` , `string`



## Tuple

하나의 항목으로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만듭니다.

```python
single_tuple = 'hello',
print(type(single_tuple))
```

```
>>> <class 'tuple'>
```



## Non-sequence Container

- 종류 : `set` , `dictionary`



## Dictionary

`key`는 **변경 불가능(immutable)한 데이터**만 가능하다. (immutable : string, integer, float, boolean, tuple, range)



## Immutable

- 리터럴(literal)
  - 숫자(Number)
  - 글자(String)
  - 참/거짓(Bool)
- range()
- tuple()

```python
# immutable 데이터의 복사는 어떻게 이루어질까?
num1 = 20
num2 = num1 
num2 = 10

print(num1)
print(num2)
```

```
20
10
```

## Mutable

- `list`
- `dict`
- `set`

```python
# mutable 데이터의 복사는 어떻게 이루어질까?
num1 = {1, 2, 3, 4}
num2 = num1
num2.add(5)

print(num1)
print(num2)
```

```
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
```


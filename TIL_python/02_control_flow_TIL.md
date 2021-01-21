# 제어문 (Control Statement)

- 이전에는 몰랐던, 혹은 헷갈렸던 내용 위주로 정리함
- 싸피의 `ipynb` 파일 내용을 다시 정리함

## 조건 표현식

- 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용된다.
- **삼항 연산자(Ternary Operator)**라고 부르기도 한다.
- `if` 절과 `else` 절에 한 줄만 있을 때 쓰기 편하다.

```python
num = -10
value = num if num >= 0 else -num
print(value)
```

```
10
```

- 작성 방법

1. 조건을 작성한다. 위 식의 경우 `num >= 0`
2. 조건 앞에 `if` 를, 뒤에 `else` 를 붙인다 `if num >= 0 else` 
3. `if` 앞에 조건에 맞으면 반환(return)해야 하는 값을 적어주고, 조건에 맞지 않으면 반환해야 하는 값은 `else` 뒤에 적는다 `num if num >= 0 else -num` 

## `else`

- 반복에서 리스트의 소진이나 (`for` 의 경우) 조건이 거짓이 돼서 (`while` 의 경우) 종료할 때 실행된다.
- 하지만 반복문이 **`break` 문으로 종료될 때는 실행되지 않는다.** (즉, `break`를 통해 중간에 종료되지 않은 경우만 실행)

### `for-else`

```python
numbers = [1, 3, 5, 7, 9]
for number in numbers:
    if number == 4:
        print(True)
        break
else:
    print(False)
```

```
False
```




# 문자열 String

## ASCII

- American Standard Code for Information Interchange

- 네트워크가 발전함에 따라 지역별 코드체계의 차이로 인한 혼란이 많아져 미국에서 제정한 인코딩 표준
- 7bit : 128문자 표현 가능, 33개의 출력 불가능한 문자와 95개의 출력 가능한 문자(공백 포함)
- 외워두면 좋을 아스키 코드들
  - 0의 ASCII : 48
  - A의 ASCII : 65
  - a의 ASCII : 97

이후 다국어 처리를 위한 표준을 만듦 => **유니코드**

## 파이썬의 문자처리

- `char` 데이터 타입이 존재하지 않고, 텍스트 데이터 처리 방법이 통일되어 있음
- `+` 를 통해 연결(Concatenation), `*` 를 통해 반복이 가능
- 시퀀스 자료형이기 때문에 인덱싱, 슬라이싱 가능

### 문자열 뒤집기

```python
word = 'python'

# 1
print(word[::-1])

# 2
new_word = ''
for idx in range(len(python)-1 , -1, -1):
    new_word += word[idx]
print(new_word)

# 3
print(''.join(list(reversed(word))))

# 4
word_list = list(word)
for idx in range(len(word_list)//2):
    word_list[idx], word_list[len(word_list) - idx - 1] = word_list[len(word_list) - idx - 1], word_list[idx]
print(''.join(word_list))
```

### 문자열 비교

파이썬에서는 `==` 연산자와 `is` 연산자 사용 가능

`==` 는 내부적으로 특수 메서드 `__eq__` 호출

```python
word1 = 'python'
word2 = 'python'
print(word1 == word2)
print(word1 is word2)
# 둘 다 True
```

### 문자열 교체

`int()` , `str()` 를 사용하지 않더라도, ASCII 코드를 이용해 처리할 수 있다!

- `ord()` : 문자를 인자로 받아 해당하는 아스키 코드 반환
- `chr()` : 숫자(아스키 코드)를 인자로 받아 해당하는 문자 반환

1. `str` => `int`

```python
def atoi(word):
    answer = 0
    i = 0
    for idx in range(len(word)-1, -1, -1):
        answer += (ord(word[idx]) - ord('0')) * (10**i)
        i += 1
    return answer

word = '123'
number = atoi(word)
print(number, type(number))
# 123 <class 'int'>
```

2. `int` => `str`

```python
def itoa(number):
    answer = ''
    # 양수
    if nunmber >= 0:
        while number:
            answer = chr(number % 10 + ord('0')) + answer
            number //= 10
        return answer
    # 음수
    else:
        number = -number
        while number:
            answer = chr(number % 10 + ord('0')) + answer
            number //= 10
        return '-' + answer
      
number = 123
word = itoa(number)
print(word2, type(word2))
# 123 <class 'str'>
```



## 패턴 매칭

- 고지식한 알고리즘(Brute Force Algorithm)
  - 본문 문자열을 처음부터 끝까지 순서대로 순회하며 패턴 내의 문자를 일일이 확인하는 방법 => 완전탐색적 접근
  - 시간복잡도 : O(NM) => 패턴의 길이 * 본문의 길이

- KMP 알고리즘
  - 불일치가 발생한 문자열 앞까지의 문자를 알고 있으므로 해당 정보를 이용하자는 아이디어에서 개발된 알고리즘
  - 패턴의 길이가 길면 성능이 좋음
  - 패턴을 전처리하여 이동할 다음 위치 중 필요하지 않은 경우 미리 줄임
  - 시간 복잡도 : O(N + M) => 패턴의 길이 + 본문의 길이
- 보이어-무어 알고리즘
  - 대부분의 사용 소프트웨어에서는 이 방법을 사용
  - 패턴의 뒤부터 확인한 후, 불일치가 발생한 부분에 해당하는 본문의 글자를 패턴이 (다른 인덱스에) 가지고 있을 경우 해당 위치(글자가 맞도록)로 이동

> 참고 : 빅오 표기법 외의 수행시간 표기

$$
\Theta(n) : 최악의 \ 경우 \ 수행시간 \\
\Omega(n) : 최선의 \ 경우 \ 수행시간
$$

보이어 무어 알고리즘의 경우 최악의 경우 O(MN)의 시간복잡도를 가지지만, 최선의 경우 O(N)을 가짐
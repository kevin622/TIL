# 데이터 구조(Data Structure) II

`set`과 `dict` : mutable, iterable, un-ordered(not sequential)

## Set

- `.add(elem)`
- `.update(iterable)`
- `.remove(elem)` : 없으면 KeyError
- `.discard(elem)` : 없어도 에러 발생하지 않음
- `.pop()` : 임의의 원소를 제거해 반환



## Dictionary

- `.get(key[, default=None])` : 절대로 KeyError가 발생하지 않음
- `.pop(key[, default])` : 없으면 KeyError, 하지만 없을 경우 반환값 지정 가능
- `.update(**kwargs[key=value])` 또는 `.update({key: value})`

### comprehension 방법

```python
# {키: 값 for 요소 in iterable if 조건식}
# {키: 값 if 조건식 else 값 for 요소 in iterable}

dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}
# 미세먼지 농도 80 초과인 곳의 밸류값을 '나쁨', 나머지는 '보통'으로 바꾸기
{key: '나쁨' if value > 80 else '보통' for key, value in dusts.items()}
# {'서울': '보통', '대전': '나쁨', '구미': '보통', '광주': '보통', '중국': '나쁨'}
```


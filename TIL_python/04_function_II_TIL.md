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


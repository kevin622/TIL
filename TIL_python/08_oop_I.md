# OOP I

객체 지향 프로그래밍

## 객체

파이썬에서 모든 것은 객체이다. 객체는 다음과 같은 특징을 갖는다.

> 타입(type), 속성(attribute), 조작법(method)

- **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가?
- **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
- **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?

### 타입type과 인스턴스instance

- 타입 : 공통된 속성과 조작법을 가진 객체들의 분류
- 인스턴스 : 특정 타입의 실제 데이터 예시(instance), 모든 객체는 특정 타입의 인스턴스임

```python
number = 10
isinstance(number, int)
```



### 속성attribute과 메서드method

- 속성 : 객체의 상태/데이터
- 메서드 : 특정 객체에 적용할 수 있는 행위(behavior)



### 클래스class와 객체object

- 클래스 : 객체들의 분류(`type`)를 정의할 때 쓰이는 키워드
- 클래스 내부에 정의한 데이터는 **속성**, 정의한 함수는 **메서드**

```python
class Person:
  def __init__(self, name):
    self.name = name
    
# instance
kevin = Person('Kevin')

print(type(kevin))
```

```
__main__.Person
```

## 메서드

`self` : **매개변수**, 인스턴스 메서드의 첫 인자로 호출되는 인스턴스 자체를 뜻함,

### 매직 메서드

더블 언더스코어를 사용하는, 특별한 일을 하는 메서드

- `__init__` : 생성자 메서드 constructor method
- `__del__` : 소멸자 메서드 destructor method
- `__str__` , `__repr__` : 특정 개체를 출력할 때 보여줄 내용

```python
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'<사람: {self.name}>'
    
    def __repr__(self):
        image = '''
          o
         /|\\
         / \\
        '''
        return image

john = Person('john')
print(john)
# <사람: john>
john
# 
#           o
#          /|\
#          / \
```


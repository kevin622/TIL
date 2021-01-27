# 객체 지향 프로그래밍



객체란? Object?

물건, 물체, 사물



`my_lower('Hi')` vs `'Hi'.lower()` 

함수의 인자로 받아져 리턴 vs 목적이 되는 대상(객체)이 **주어**가 된다.

`sorted([3, 2, 1])` vs `[3, 2, 1].sort()`



절차 지향 프로그래밍

직사각형 넓이 구하기

```python
def area(x, y):
  return x * y
```

x, y값이 함수 인자로 들어감



```python
class Rectangle:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
    return self.x * self.y

r1 = Rectangle(10,30)
r1.area()
```



클래스 

사람

​	정보 : 이름, 나이...

​	행동 : 말하기,...
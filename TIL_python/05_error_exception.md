# 에러 / 예외처리



## 에러 종류

### 문법 에러 Syntax Error

> 실행 자체가 되지 않는다!

```python
if True print('참')
# SyntaxError: invalid syntax

print('Hi)
# SyntaxError: EOL while scanning string literal
# EOL - 따옴포 에러
      
print('Hi'
# SyntaxError: unexpected EOF while parsing
# EOf - 괄호닫기 에러
```



### 예외 Exception

> 예상하지 못한 상황(Exception)을 맞이하면 프로그램이 멈춤

```python
10 * (1/0)
# ZeroDivisionError: division by zero

print(abc)
# NameError: name 'abc' is not defined

1 + '1'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 자료형에 대한 에러




```


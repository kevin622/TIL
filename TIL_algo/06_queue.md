# 큐 Queue

- 선입선출 FIFO
- `front` : 마지막으로 자료가 없어진(deQueue) 위치
- `rear` : 마지막으로 자료가 삽입된(enQueue) 위치

## 선형 큐

- 배열 이용
- 초기 : `front` = `rear` = -1

```python
N = 8
queue = [0] * N
front = -1
rear = -1


def is_empty():
    return front == rear


def is_full():
    return rear == N


def en_queue(number):
    if is_full():
        print('Queue is Full')
    else:
        global rear
        rear += 1
        queue[rear] = number


def de_queue():
    if is_empty():
        print('Queue is Empty')
    else:
        global front
        front += 1
        return queue[front]

en_queue(1)
en_queue(2)
en_queue(3)
print(queue)
# [1, 2, 3, 0, 0, 0, 0, 0]

print(de_queue())
# 1
print(de_queue())
# 2
print(de_queue())
# 3
print(queue)
# [1, 2, 3, 0, 0, 0, 0, 0]
```

- 단점

    - 배열의 앞 부분에 활용이 가능한 공간이 있음에도 포화상태로 인식할 수 있음

        (`rear` == N-1)

    - 연산이 발생할 때마다 배열을 앞 부분으로 이동시킴으로 이를 방지할 수 있지만, 매우 비효율적임

## 원형 큐

- 1차원 배열이지만, 논리적으로 배열의 끝과 처음이 연결되어 있는 원형 형태의 큐를 이룬다고 가정
- 초기 : `front` = `rear` = 0
- 나머지 연산자 `%` 를 사용하여 마지막 인덱스인 `N-1` 다음이 `0`이 나오도록 함

```python
# 선형 큐 삽입, 삭제 위치
rear = rear + 1
front = front + 1

# 원형 큐 삽입, 삭제 위치
rear = (rear + 1) % N
front = (front + 1) % N
```

- `front` 의 위치는 항상 비어있음, 따라서 full 과 empty의 조건이 다음과 같음

```python
def isEmpty():
    return rear == front

def isFull():
    return (rear + 1) % N == front
```



> 연결 큐,  우선순위 큐는 나중에 배운다!



## BFS 너비 우선 탐색

**Breadth First Search**

![BFS](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc305k7%2FbtqB5E2hI4r%2Fea7vFo08tkDYo4c8wkfVok%2Fimg.gif)

```python
def BFS(G, v):
    visited = [0] * n
    queue = [v]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = 1
            for w in G[node]:
                if not visited[w]:
                    queue.append(w)
```

- 미로에서 최단거리를 찾는 경우라면?

```python
visited = [0] * n
queue = [[v]]
turn = 0  # 지난 간선의 수를 계산할 변수
while queue[0]:
  	turn += 1
    nodes = queue.pop(0)
    temp = []
    for node in nodes:
        if not visited[node]:
            visited[node] = 1
            for w in G[node]:
                if not visited[w]:
                    temp.append(w)
                    G[w] = turn. # 현재 위치에 현재 지난 간선 수 표시
    queue.append(temp)
```


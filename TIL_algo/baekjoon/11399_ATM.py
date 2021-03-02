N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
answer = 0
for i in range(1, N + 1):
    answer += sum(numbers[:i])
print(answer)
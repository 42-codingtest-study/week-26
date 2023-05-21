n = int(input())

lst = [int(input()) for i in range(n)]
stack = []
answer = 0

for i in range(n):
    while stack and stack[-1] <= lst[i]:
        stack.pop()

    stack.append(lst[i])
    answer += len(stack) - 1

print(answer)

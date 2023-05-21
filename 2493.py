N = int(input())
lst = [*map(int, input().split())]
stack = []
answer = [0 for i in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1] > lst[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, lst[i]])

print(*answer)

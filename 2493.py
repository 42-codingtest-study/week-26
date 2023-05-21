import sys

n = int(input())
tower = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
    t = tower[i]
    while stack and tower[stack[-1]] < t:
        print("stack : ", stack[-1])
        print("tower stack : ",tower[stack[-1]])    
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, answer))))
        
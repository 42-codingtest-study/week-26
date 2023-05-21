# 05강_옥상 정원 꾸미기

import sys

input = sys.stdin.readline
N = int(input())
stack = []
ans = 0

for _ in range(N):
    tower = int(input())
    if stack:
        if stack[-1] <= tower:
            while stack and stack[-1] <= tower:
                stack.pop()
            ans += len(stack)
            stack.append(tower)
        else:
            ans += len(stack)
            stack.append(tower)
    else:
        stack.append(tower)
print(ans)
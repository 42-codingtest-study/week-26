# 05강_오큰수

import sys

input = sys.stdin.readline
n = int(input())
stack = list(map(int, input().split()))
targets = []
ans = [-1] * n

idx = 0
stack.reverse()
targets.append((idx, stack.pop()))

while stack:
    t = stack.pop()
    idx += 1

    while targets and targets[-1][1] < t:
        a, b = targets.pop()
        ans[a] = t
    
    targets.append((idx, t))

for i in ans:
    print(i, end=' ')
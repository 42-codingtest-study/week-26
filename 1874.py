# 05강_스택 수열

import sys
N = int(sys.stdin.readline())
stack = [] 
start = 1
operator = []

for _ in range(N):
    end = int(sys.stdin.readline())
    while start <= end: 
        stack.append(start) 
        operator.append('+')
        start += 1
    
    if stack[-1] == end :
        stack.pop() 
        operator.append('-')
    
    else : 
        print("NO") 
        break

else :
    for i in operator :
        print(i)
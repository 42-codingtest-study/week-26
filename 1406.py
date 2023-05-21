# 04강_에디터

left = list(input())
right = []
n = len(left)
m = int(input())

for m in range(m):
    ord = list(input().split())

    if ord[0] == 'L':              
        if left:                       
            right.append(left.pop())     
    elif ord[0] == 'D':            
        if right:                       
            left.append(right.pop())     
    elif ord[0] == 'B':          
        if left:
            left.pop()
    else:                         
        left.append(ord[1])

left.extend(reversed(right))
print(''.join(left))
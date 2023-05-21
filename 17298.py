n = int(input())
lst = list(map(int, input().split()))
res_list = [-1] * n
stack = []

for i in range(n):
    while stack and lst[stack[-1]] < lst[i]:
        res_list[stack.pop()] = lst[i]
    print("1",stack)
    print("1", *res_list)
    
    stack.append(i)
    print("2",stack)
    print("2", *res_list)
    
    
print(*res_list)

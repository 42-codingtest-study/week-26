n = int(input())
height = []
stack = []
res = 0
for i in range(n):
    height.append(int(input()))

for i in height:
    while stack and stack[-1] <= i:
        # print("stack in:" , stack[-1])
        stack.pop()
    stack.append(i)
    # print("stack out:" , stack[-1])
    
    # print(stack)
    res += len(stack) -1
    # print("len : ", res)
    
print(res)
            
# for i in range(n):
#     t = tower[i]
#     while stack and tower[stack[-1]] < t:
#         # print("stack : ", stack[-1])
#         # print("tower stack : ",tower[stack[-1]])    
#         stack.pop()
#     if stack:
#         answer[i] = stack[-1] + 1
#     stack.append(i)

# print(' '.join(list(map(str, answer))))
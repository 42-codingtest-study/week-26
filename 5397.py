n = int(input())
for i in range(n):
    password = input()
    left, right = [], []
    for idx in password:
        if idx == '<':
            if left:
                right.append(left.pop())
                print("right : ", right)
                
        elif idx == '>':
            if right:
                print("left before : ", left)
                left.append(right.pop())
                print("left : ", left)
                # print("right : ", right)
                
        elif idx == '-':
            if left:
                left.pop()
        else:
            left.append(idx)
    left.extend(reversed(right))
    print(''.join(left))
        
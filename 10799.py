stick = list(input())
cnt, curr = 0, 0
lst = []
for i in stick:
    if i == "(":
        lst.append("(")
        curr += 1
    else:
        lst.append(")")
        if lst[-1] == ")" and lst[-2] == "(":
            curr -= 1
            cnt += curr
        else:
            cnt += 1
            curr -= 1
print(cnt)

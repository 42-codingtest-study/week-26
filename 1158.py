n, k = map(int, input().split())
k -= 1
num = 0
people = []
left = []

for i in range (n):
    people.append(i+1)

for i in range(n):
    num += k
    if num >= len(people):
        num = num % len(people)
    
    left.append(str(people.pop(num)))

print("<",", ".join(left)[:],">", sep='')

import sys
input = sys.stdin.readline

stack = []
si = 0
result = []

def push(num):
    stack.append(num)
    result.append('+')

def pop():
    stack.pop(len(stack)-1)
    result.append('-')

t = int(input())
for _ in range(t) :
	k = int(input())
	if len(stack) == 0 :
		for i in range(si + 1, k+1) :
			push(i)
		si = k
		pop()
	else :
		last = len(stack)-1
		if stack[last] == k:
			pop()
		elif stack[last] < k:
			for i in range(si + 1, k+1) :
				push(i)
			si = k
			pop()
		else :
			print("NO")
			exit()

print('\n'.join(result))

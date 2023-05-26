import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

t = int(input())

def dfs(per):
	global result
	global cycle
	if not visit[per] :
		cycle.append(per)
		visit[per] = True
		dfs(want[per])
	else :
		for i in range(len(cycle)):
			if cycle[i] == per:
				result += cycle[i:]


for _ in range (t):
	n = int(input())
	visit = [True] + [False] * n
	want = [0] + list(map(int,input().rstrip().split()))
	result = []
	for i in range(1, n+1):
		if i not in result :
			cycle = []
			dfs(i)

	print(n - len(result))

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

T = int(input())

def dfs(x, y):
	if x < 0 or x >= m or y < 0 or y >= n :
		return False
	if graph[y][x] == 1 :
		graph[y][x] = 0
		dfs(x - 1, y)
		dfs(x + 1, y)
		dfs(x , y - 1)
		dfs(x , y + 1)
		return True
	return False

for _ in range (T):
	m, n, k = map(int, input().split())
	graph = [[0 for _ in range(m)] for _ in range(n)]
	for i in range(k):
		x, y = map(int, input().split())
		graph[y][x] = 1

	bugs = 0
	for y in range (n) :
		for x in range (m) :
			if dfs(x, y):
				bugs += 1
	print(bugs)

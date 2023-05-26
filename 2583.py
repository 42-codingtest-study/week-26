import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
	s_x, s_y, e_x, e_y = map(int, input().split())
	for y in range(s_y, e_y) :
		for x in range(s_x, e_x) :
			graph[y][x] = 1

def dfs(x, y):
	global cnt
	if x < 0 or x >= n or y < 0 or y >= m :
		return False
	if graph[y][x] == 0 :
		graph[y][x] = 1
		cnt += 1
		dfs(x + 1, y)
		dfs(x - 1, y)
		dfs(x, y + 1)
		dfs(x, y - 1)
		return True
	return False

spot = 0
cnt = 0
area = []
for y in range(m) :
	for x in range(n):
		if dfs(x, y) :
			spot += 1
			area.append(cnt)
			cnt = 0

print(spot)
area.sort()
print(' '.join(map(str, area)))

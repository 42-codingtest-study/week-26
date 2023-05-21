import sys

sys.setrecursionlimit(10**6)


def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and picture[nx][ny] == 1:
            dfs(nx, ny)


N, M = map(int, input().split())

picture = []
for _ in range(N):
    picture.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0
max_area = 0
cnt = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and picture[i][j] == 1:
            dfs(i, j)
            max_area = max(max_area, count)
            count = 0
            cnt += 1

print(cnt)
print(max_area)

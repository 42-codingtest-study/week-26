# 그림

def dfs(x, y) :
    a[x][y] == 0
    graph_x = [1, -1, 0, 0]
    graph_y = [0, 0, 1, -1]
    w = 1
    q = list()
    q.append([x, y])
    while q :
        x, y = q.pop()
        for i in range(4):
            nx = graph_x[i] + x
            ny = graph_y[i] + y
            if 0 <= nx < x and 0 <= ny < y and a[nx][ny] == 1:
                    q.append([nx, ny])
                    a[nx][ny] = 0
                    w += 1
    return w
        
x, y = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(x)]

cnt = 0
res = 0

for i in range(x) :
    for j in range(y) :
        if a[i][j] == 1:
            cnt += 1
        res = max(dfs(i, j), res)

print(cnt)
print(res)  
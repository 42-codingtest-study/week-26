n, m = map(int, input().split())

graph = []
for _ in range (n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    global tmp
    if x < 0 or x >= m or y < 0 or y >= n :
        return False
    if graph[y][x] == 1 :
        graph[y][x] = 0
        tmp += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

draw = 0
large = 0
for y in range (0, n) :
    for x in range (0, m) :
        tmp = 0
        if dfs(x, y) == True :
            draw += 1
            large = max(large, tmp)

print (draw)
print (large)
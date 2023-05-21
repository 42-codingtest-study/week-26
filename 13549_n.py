import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dist = dict()
dist[n] = 0

def bfs(start):
    q = deque()
    q.append(start)
    while q :
        cur = q.popleft()
        flag = 0
        for nx in (cur - 1, cur * 2, cur + 1):
            flag += 1
            if nx < 0 or nx > 100000 :
                continue
            if nx == k :
                if flag % 2 :
                    return dist[cur] + 1
                else :
                    return dist[cur]
            if not nx in dist :
                if flag % 2 : 
                    dist[nx] = dist[cur] + 1
                else :
                    dist[cur * 2] = dist[cur]
                q.append(nx)

if n == k :
    print(0)
else :
    print(bfs(n))
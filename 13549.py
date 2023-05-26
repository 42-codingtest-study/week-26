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
        if cur * 2 == k :
            return dist[cur]
        if not cur * 2 in dist :
            if cur * 2 >= 0 and cur * 2 <= 100000 :
                q.append(cur * 2)
                dist[cur * 2] = dist[cur]
        for nx in (cur - 1, cur + 1):
            if nx < 0 or nx > 100000 :
                continue
            if nx == k :
                return dist[cur] + 1
            if not nx in dist : 
                dist[nx] = dist[cur] + 1
                q.append(nx)

if n == k :
    print(0)
else :
    print(bfs(n))
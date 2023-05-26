from collections import deque, defaultdict

n, k = map(int, input().split())
dist = {} # dist = dict() 로 표현 가능
dist[n] = 0
route = {}
route[n] = []
route[n].append(n)

def bfs(start) :
    q = deque()
    q.append(start)
    while q :
        i = q.popleft()
        for su in (i - 1, i + 1, 2 * i) :
            if su < 0 or su > 100000 : #메모리 초과되기 싫으면 넣어라 좌식아
                continue
            if su == k :
                route[su] = route[i].copy()
                route[su].append(su)
                return dist[i] + 1
            if not su in dist :
                route[su] = route[i].copy()
                route[su].append(su)
                dist[su] = dist[i] + 1
                q.append(su)

if n == k :
	print(0)
	print(' '.join(map(str, route[k])))
else :
	print(bfs(n))
	print(' '.join(map(str, route[k])))

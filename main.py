from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input())
dist = [-1] * n
dist[start] = 0

q = deque([start])
while q:
    node = q.popleft()
    for nei in graph[node]:
        if dist[nei] == -1:
            dist[nei] = dist[node] + 1
            q.append(nei)

print(*dist)

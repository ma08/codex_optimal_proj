

from collections import defaultdict

def dfs(v, p):
	global graph, n, k, count, ans, comp
	for u in graph[v]:
		if u == p:
			continue
		dfs(u, v)
		if count[u] > k:
			ans = -1
			return
		count[v] += count[u]
		comp[u] = comp[v]
	if n - count[v] > k:
		ans = -1
		return
	if n - count[v] > 0:
		ans += 1
		comp[v] = ans
	
n, k = map(int, input().split())
graph = defaultdict(list)
for i in range(n-1):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)
count = [0 for i in range(n+1)]
count[1] = 1
comp = [0 for i in range(n+1)]
ans = 0
dfs(1, 0)

if ans == -1:
	print(-1)
else:
	print(ans)
	print(*comp[2:])
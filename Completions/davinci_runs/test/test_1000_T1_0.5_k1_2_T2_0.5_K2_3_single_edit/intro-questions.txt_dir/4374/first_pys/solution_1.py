
from collections import defaultdict

def dfs(v, p):
	global max_d, max_v
	d = 0
	for u in graph[v]:
		if u != p:
			dd = dfs(u, v)
			d = max(d, dd)
			if dd > max_d:
				max_d = dd
				max_v = u
	return d + 1

def dfs2(v, p, d):
	global max_d
	max_d = max(max_d, d)
	for u in graph[v]:
		if u != p:
			dfs2(u, v, d + 1)

def main():
	global graph, max_d, max_v
	n, m = map(int, input().split())
	graph = defaultdict(list)
	for _ in range(m):
		v, u = map(int, input().split())
		graph[v].append(u)
		graph[u].append(v)

	max_d = 0
	max_v = 0
	dfs(1, 0)
	max_d = 0
	dfs2(max_v, 0, 0)
	print(max_d)

	for v in range(1, n + 1):
		for u in graph[v]:
			if v < u:
				print(v, u)

main()
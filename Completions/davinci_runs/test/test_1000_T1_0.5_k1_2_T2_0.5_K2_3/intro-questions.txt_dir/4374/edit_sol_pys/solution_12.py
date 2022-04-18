from collections import defaultdict, deque

def bfs(v):
	global d
	d[v] = 0
	q = deque([v])
	while q:
		v = q.popleft()
		for u in graph[v]:
			if d[u] == -1:
				d[u] = d[v] + 1
				q.append(u)


def main():
	global graph, d
	n = int(input())
	graph = defaultdict(list)
	for _ in range(n - 1):
		v, u = map(int, input().split()) - 1
		graph[v].append(u - 1)
		graph[u - 1].append(v - 1)


	d = [-1] * n
	bfs(0)
	v = d.index(max(d))
	d = [-1] * n
	bfs(v)
	v = d.index(max(d))
	d = [-1] * n
	bfs(v)
	print(max(d))

main()

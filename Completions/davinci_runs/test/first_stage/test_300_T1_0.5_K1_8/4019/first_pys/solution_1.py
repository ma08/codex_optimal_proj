

import sys

sys.setrecursionlimit(200000)

def read_ints():
	return [int(x) for x in sys.stdin.readline().strip().split()]

def read_edge():
	return read_ints()

def read_edges(m):
	return [read_edge() for _ in range(m)]

def write_edges(edges):
	sys.stdout.write('YES\n')
	for edge in edges:
		sys.stdout.write('{} {}\n'.format(edge[0], edge[1]))

def dfs(start, graph, visited):
	visited[start] = True
	for neighbour in graph[start]:
		if not visited[neighbour]:
			dfs(neighbour, graph, visited)

def solve(n, m, D, edges):
	# TODO: Implement this function
	graph = [[] for _ in range(n + 1)]
	for edge in edges:
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])

	visited = [False for _ in range(n + 1)]
	dfs(1, graph, visited)

	if D == 0:
		if all(visited[1:]):
			write_edges([])
			return
		else:
			sys.stdout.write('NO\n')
			return

	for edge in edges:
		if edge[0] == 1:
			graph[edge[0]].remove(edge[1])
			graph[edge[1]].remove(edge[0])
			visited = [False for _ in range(n + 1)]
			dfs(1, graph, visited)
			if D == 1:
				if all(visited[1:]):
					write_edges([edge])
					return
				else:
					sys.stdout.write('NO\n')
					return
			graph[edge[0]].append(edge[1])
			graph[edge[1]].append(edge[0])
		elif edge[1] == 1:
			graph[edge[0]].remove(edge[1])
			graph[edge[1]].remove(edge[0])
			visited = [False for _ in range(n + 1)]
			dfs(1, graph, visited)
			if D == 1:
				if all(visited[1:]):
					write_edges([edge])
					return
				else:
					sys.stdout.write('NO\n')
					return
			graph[edge[0]].append(edge[1])
			graph[edge[1]].append(edge[0])

	for edge in edges:
		if edge[0] == 1:
			for edge_2 in edges:
				if edge_2[0] == 1 and edge_2[1] != edge[1]:
					graph[edge[0]].remove(edge[1])
					graph[edge[1]].remove(edge[0])
					graph[edge_2[0]].remove(edge_2[1])
					graph[edge_2[1]].remove(edge_2[0])
					visited = [False for _ in range(n + 1)]
					dfs(1, graph, visited)
					if D == 2:
						if all(visited[1:]):
							write_edges([edge, edge_2])
							return
					graph[edge[0]].append(edge[1])
					graph[edge[1]].append(edge[0])
					graph[edge_2[0]].append(edge_2[1])
					graph[edge_2[1]].append(edge_2[0])
		elif edge[1] == 1:
			for edge_2 in edges:
				if edge_2[0] == 1 and edge_2[1] != edge[0]:
					graph[edge[0]].remove(edge[1])
					graph[edge[1]].remove(edge[0])
					graph[edge_2[0]].remove(edge_2[1])
					graph[edge_2[1]].remove(edge_2[0])
					visited = [False for _ in range(n + 1)]
					dfs(1, graph, visited)
					if D == 2:
						if all(visited[1:]):
							write_edges([edge, edge_2])
							return
					graph[edge[0]].append(edge[1])
					graph[edge[1]].append(edge[0])
					graph[edge_2[0]].append(edge_2[1])
					graph[edge_2[1]].append(edge_2[0])

	sys.stdout.write('NO\n')

n, m, D = read_ints()
edges = read_edges(m)
solve(n, m, D, edges)
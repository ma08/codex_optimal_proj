

import sys
from collections import defaultdict

def dfs(v, visited):
	visited[v] = True
	for u in adj_list[v]:
		if not visited[u]:
			dfs(u, visited)

def main():
	n, m, s = map(int, sys.stdin.readline().split())
	adj_list = defaultdict(list)
	for _ in range(m):
		u, v = map(int, sys.stdin.readline().split())
		adj_list[u].append(v)
	visited = [False] * (n + 1)
	dfs(s, visited)
	count = 0
	for v in range(1, n + 1):
		if not visited[v]:
			count += 1
	print count

if __name__ == '__main__':
	main()

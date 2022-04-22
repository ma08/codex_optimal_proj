

import sys

# Using DFS to find the number of nodes that are reachable from node s
from collections import defaultdict

def dfs(v, visited):
	visited[v] = True
	for u in rev_adj_list[v]:
		if not visited[u]:
			dfs(u, visited)

def main():
	global rev_adj_list
	n, m, s = map(int, sys.stdin.readline().split())
	adj_list = defaultdict(list)
	rev_adj_list = defaultdict(list)
	for _ in range(m):
		u, v = map(int, sys.stdin.readline().split())
		adj_list[u].append(v)
		rev_adj_list[v].append(u)
	visited = [False] * (n + 1)
	dfs(s, visited)
	count = 0
	for v in range(1, n + 1):
		if not visited[v]:
			for u in adj_list[v]:  # checking if a node can reach node s
				if visited[u]:    # if a node can reach node s, then increment count
					count += 1  
					break        
	print count

if __name__ == '__main__':
	main()

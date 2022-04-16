

import sys

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.neighbors = []
		self.visited = False
		self.parent = None

	def add_neighbor(self, neighbor):
		self.neighbors.append(neighbor)

	def __str__(self):
		return "({}, {})".format(self.x, self.y)

def solve(t, grid):
	nodes = []
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] != "1":
				nodes.append(Node(i, j))

	for node in nodes:
		x, y = node.x, node.y
		if grid[x][y] == "S": # start node
			start = node
		elif grid[x][y] == "0": # normal node
			if x > 0 and grid[x-1][y] != "1":
				node.add_neighbor(nodes[(x-1) * len(grid[0]) + y])
			if x < len(grid) - 1 and grid[x+1][y] != "1":
				node.add_neighbor(nodes[(x+1) * len(grid[0]) + y])
			if y > 0 and grid[x][y-1] != "1":
				node.add_neighbor(nodes[x * len(grid[0]) + y - 1])
			if y < len(grid[0]) - 1 and grid[x][y+1] != "1":
				node.add_neighbor(nodes[x * len(grid[0]) + y + 1])
		elif grid[x][y] == "U": # up node
			if x > 0 and grid[x-1][y] != "1":
				node.add_neighbor(nodes[(x-1) * len(grid[0]) + y])
		elif grid[x][y] == "D": # down node
			if x < len(grid) - 1 and grid[x+1][y] != "1":
				node.add_neighbor(nodes[(x+1) * len(grid[0]) + y])
		elif grid[x][y] == "L": # left node
			if y > 0 and grid[x][y-1] != "1":
				node.add_neighbor(nodes[x * len(grid[0]) + y - 1])
		elif grid[x][y] == "R": # right node
			if y < len(grid[0]) - 1 and grid[x][y+1] != "1":
				node.add_neighbor(nodes[x * len(grid[0]) + y + 1])

	queue = [start]
	start.visited = True
	while len(queue) > 0:
		curr = queue.pop(0)
		if curr.x == 0 or curr.x == len(grid) - 1 or curr.y == 0 or curr.y == len(grid[0]) - 1:
			return 1
		for neighbor in curr.neighbors:
			if not neighbor.visited:
				neighbor.visited = True
				neighbor.parent = curr
				queue.append(neighbor)

	return -1

def main():
	t, n, m = map(int, sys.stdin.readline().strip().split())
	grid = []
	for _ in range(n):
		grid.append(list(sys.stdin.readline().strip()))
	
	print(solve(t, grid))

if __name__ == "__main__":
	main()

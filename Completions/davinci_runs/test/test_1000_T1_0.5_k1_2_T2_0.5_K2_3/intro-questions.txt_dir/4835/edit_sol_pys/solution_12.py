

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
			if grid[i][j] != "X":
				nodes.append(Node(j, i))

	for node in nodes:
		x, y = node.x, node.y
		if grid[x][y] == "S":
			start = node
		elif grid[x][y] == "0":
			if x > 0 and grid[x-1][y] != "X":
				node.add_neighbor(nodes[y * len(grid[0]) + x - 1])
			if x < len(grid) - 1 and grid[x+1][y] != "X":
				node.add_neighbor(nodes[y * len(grid[0]) + x + 1])
			if y > 0 and grid[x][y-1] != "X":
				node.add_neighbor(nodes[(y-1) * len(grid[0]) + x])
			if y < len(grid[0]) - 1 and grid[x][y+1] != "X":
				node.add_neighbor(nodes[(y+1) * len(grid[0]) + x])
		elif grid[x][y] == "U":
			if x > 0 and grid[x-1][y] != "X":
				node.add_neighbor(nodes[y * len(grid[0]) + x - 1])
		elif grid[x][y] == "D":
			if x < len(grid) - 1 and grid[x+1][y] != "X":
				node.add_neighbor(nodes[y * len(grid[0]) + x + 1])
		elif grid[x][y] == "L":
			if y > 0 and grid[x][y-1] != "X":
				node.add_neighbor(nodes[(y-1) * len(grid[0]) + x])
		elif grid[x][y] == "R":
			if y < len(grid[0]) - 1 and grid[x][y+1] != "X":
				node.add_neighbor(nodes[(y+1) * len(grid[0]) + x])

	queue = [start]
	start.visited = True
	while len(queue) > 0:
		curr = queue.pop(0)
		if curr.x == 0 or curr.x == len(grid[0]) - 1 or curr.y == 0 or curr.y == len(grid) - 1:
			if t >= 1:
				return 1
			else:
				return 0
		for neighbor in curr.neighbors:
			if not neighbor.visited:
				neighbor.visited = True
				neighbor.parent = curr
				if neighbor.x == 0 or neighbor.x == len(grid[0]) - 1 or neighbor.y == 0 or neighbor.y == len(grid) - 1:
					if t >= 1:
						return 1
					else:
						return 0
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

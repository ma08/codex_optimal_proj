

import numpy as np

def main():
	H, W, K = map(int, input().split())
	grid = []
	for i in range(H):
		grid.append(list(input()))
	grid = np.array(grid)
	grid = np.vectorize(lambda x: 0 if x == '.' else 1)(grid)

	count = 0
	for i in range(2**H):
		for j in range(2**W):
			row = np.array(list(map(int, bin(i)[2:].zfill(H))))
			col = np.array(list(map(int, bin(j)[2:].zfill(W))))
			# print(row, col)
			# print(row[:,np.newaxis])
			# print(np.dot(row[:,np.newaxis], col))
			# print(grid + np.dot(row[:,np.newaxis], col))
			# print(np.sum(grid + np.dot(row[:,np.newaxis], col)))
			if np.sum(grid + np.dot(row[:,np.newaxis], col)) == K:
				count += 1
	print(count)

if __name__ == '__main__':
	main()

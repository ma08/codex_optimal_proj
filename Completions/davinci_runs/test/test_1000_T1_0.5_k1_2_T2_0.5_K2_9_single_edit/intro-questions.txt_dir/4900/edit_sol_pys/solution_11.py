


def solve(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(i+1, n):
			if matrix[i][j] == 1:
				print(i+1, j+1)


def main():
	n = int(input())
	matrix = []
	for _ in range(n):
		matrix.append([int(x) for x in input().split()])
	solve(matrix)

if __name__ == '__main__':
	main()

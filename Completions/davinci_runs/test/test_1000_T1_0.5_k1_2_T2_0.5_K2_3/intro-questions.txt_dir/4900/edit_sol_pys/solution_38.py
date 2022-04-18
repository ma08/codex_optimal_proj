

def main():
	n = int(input())
	matrix = []
	for _ in range(n):
		matrix.append([int(x) for x in input().split()])
	for i in range(n):
		for j in range(i+1, n):
			if matrix[i][j] == 1:
				print(j+1, i+1) 

if __name__ == '__main__':
	main()

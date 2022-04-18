

def main():
	n, r = map(int, input().split())
	projects = []
	for i in range(n):
		a, b = map(int, input().split())
		projects.append((a, b))

	projects.sort(key = lambda x: x[1])

	count = 0
	for i in range(n):
		if r >= projects[i][0]:
			r += projects[i][1]
			count += 1
		else:
			break

	print(count)

if __name__ == '__main__':
	main()

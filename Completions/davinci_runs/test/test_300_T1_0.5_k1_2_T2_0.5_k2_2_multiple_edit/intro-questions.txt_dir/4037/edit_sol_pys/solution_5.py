

def main():
	n, s = map(int, input().split())
	projects = []
	for i in range(n):
		a, b = map(int, input().split())
		projects.append((a, b))

	projects.sort(key = lambda x: x[0])

	count = 0
	for project in projects:
		if s > project[0]:
			s += project[1]
			count += 1
		else:
			break

	print(count)

if __name__ == '__main__':
	main()

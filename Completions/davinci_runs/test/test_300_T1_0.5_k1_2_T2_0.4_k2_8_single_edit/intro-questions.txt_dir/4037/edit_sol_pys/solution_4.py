

def main():
	n, r = map(int, input().split())
	projects = []
	for i in range(n):
		a, b = map(int, input().split())
		projects.append([a, b])

	projects.sort(key = lambda x: x[0])

	count = 0
	for project in projects:
		if r < project[0]:
			continue
		r += project[1]
		count += 1

	print(count)

if __name__ == '__main__':
	main()

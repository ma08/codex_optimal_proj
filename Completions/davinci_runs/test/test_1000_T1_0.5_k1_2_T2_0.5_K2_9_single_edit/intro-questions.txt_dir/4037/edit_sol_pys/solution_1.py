

def solve(n, r, projects):
	projects.sort(key = lambda x: x[0])

	count = 0
	for project in projects:
		if r >= project[0]:
			r += project[1]
			count += 1
		else:
			break

	return count

def main():
	n, r = map(int, input().split())
	projects = []
	for i in range(n):
		a, b = map(int, input().split())
		projects.append((a, b))

	print(solve(n, r, projects))

if __name__ == '__main__':
	main()

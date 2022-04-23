
def is_possible(r, projects):
	for project in projects:
		if r < project[0]:
			return False
		r += project[1]
	return True


def main():
	n, r = map(int, input().split()) # n is number of projects and r is initial rating
	projects = []
	for i in range(n):
		a, b = map(int, input().split())
		projects.append((a, b))

	projects.sort(key = lambda x: x[0])

	low = 0
	high = n
	while low < high:
		mid = (low + high) // 2
		if is_possible(r, projects[:mid]):
			high = mid
		else:
			low = mid + 1

	print(low)

if __name__ == '__main__':
	main()

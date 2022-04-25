

def main(): 
	n, r = map(int, input().split())
	projects = []
	for i in range(n):
		a, b = map(int, input().split()) # a = deadline, b = points
		projects.append((b, a))

	projects.sort(key = lambda x: x[0], reverse=True) # sort by points

	count = 0
	for project in projects:
		if r <= project[1]: # deadline
			r += project[0] # points
			count += 1
		else:
			break

	print(count)

if __name__ == '__main__':
	main()

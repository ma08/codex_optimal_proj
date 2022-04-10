

def get_min_packages(n, k):
	if n == 1:
		return 1
	if k == 1:
		return n
	if n <= k:
		return 1
	if n % 2 == 0:
		if k >= n/2:
			return 2
		return get_min_packages(n, k-1)
	else:
		if k >= (n+1)/2:
			return 2
		return get_min_packages(n, k-1)

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n, k = map(int, input().split())
		print(get_min_packages(n, k))
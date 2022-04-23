

import random, sys

def resolve(n, a):
	p = random.randint(0, n-1)
	q = random.randint(0, n-1)
	while p == q:
		q = random.randint(0, n-1)
	a[q] -= a[p]
	return a

def main():
	n = int(sys.stdin.readline())
	a = list(map(int, sys.stdin.readline().split()))
	while True:
		a = resolve(n, a)
		if a.count(0) == n-1:
			print(a[a.index(max(a))])
			break

if __name__ == '__main__':
	main()

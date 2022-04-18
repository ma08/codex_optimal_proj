

import random

def resolve(n, a):
	p = random.randint(0, n-1)
	q = random.randint(0, n-1)
	while p == q:
		q = random.randint(0, n-1)
	a[q] -= a[p]
	return a[q]

def main():
	n = int(input())
	a = list(map(int, input().split()))
	while True:
		b = resolve(n, a)
		if b.count(0) == n-1:
			print(b[b.index(max(b))])
			break

if __name__ == '__main__':
	main()



import sys

def main():
	n, m = map(int, sys.stdin.readline().split())

	a = []
	for i in range(n):
		a.append(map(int, sys.stdin.readline().split()))

	a.sort(key=lambda x: max(x))

	s = []
	for i in range(m):
		for j in range(n):
			s.append(a[j][i])

	k = 0
	for i in range(len(s) - 1):
		k = max(k, abs(s[i] - s[i + 1]))

	print k

if __name__ == '__main__':
	main()
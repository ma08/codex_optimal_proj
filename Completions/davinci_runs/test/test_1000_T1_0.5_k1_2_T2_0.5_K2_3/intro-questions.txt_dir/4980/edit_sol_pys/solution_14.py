#http://codeforces.com/problemset/problem/1155/B

import math
import sys

def main():

	n, k = map(int, sys.stdin.readline().split())
	a = list(map(int, sys.stdin.readline().split()))
	a.sort()
	a.reverse()
	count = 1
	total = a[0]
	i = 1
	while i < n and total < k:
		total += a[i]
		count += 1
		i += 1

	if count == 0:
		print(-1)
	else:


		print(count)

main()

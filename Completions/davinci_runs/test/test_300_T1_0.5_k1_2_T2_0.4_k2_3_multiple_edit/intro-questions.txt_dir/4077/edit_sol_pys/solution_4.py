#!/usr/bin/env python3

import sys

def median(arr):
	n = len(arr)
	if n < 1:
		return None
	if n % 2 == 1:
		return sorted(arr)[n//2]
	else:
		return sum(sorted(arr)[n//2-1:n//2+1])/2.0

def main():
	n, m = [int(x) for x in sys.stdin.readline().split()]
	arr = [int(x) for x in sys.stdin.readline().split()]
	pairs = 0
	for i in range(n):
		for j in range(i, n):
			if median(arr[i:j+1]) == m:
				pairs += 1
	print(pairs)

if __name__ == '__main__':
	main()

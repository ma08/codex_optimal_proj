#!/usr/bin/env python3


def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))

	def concat(x, y):
	    return (x * 10**len(str(y))) + y

	def count_divisible(x):
	    count = 0
	    for i in range(n):
	        if concat(x, a[i]) % k == 0:
	            count += 1
	    return count

	total = 0
	for i in range(n):
	    total += count_divisible(a[i])

	print(total)

if __name__ == '__main__':
	main()

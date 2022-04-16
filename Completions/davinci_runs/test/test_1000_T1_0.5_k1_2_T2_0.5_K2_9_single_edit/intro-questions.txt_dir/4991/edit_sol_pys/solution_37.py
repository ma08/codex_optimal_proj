

#!/usr/bin/env python

def hailstone(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return n + hailstone(n // 2)
	else:
		return n + hailstone((3 * n) + 1)

def main():
	n = int(input())
	print(hailstone(n))

if __name__ == '__main__':
	main()


import sys

def main():
	d, n = map(int, sys.stdin.readline().split())
	if d == 0:
		print(n)
	elif d == 1:
		print(100 * n)
	else:
		print(10000 * n)

if __name__ == '__main__':
	main()

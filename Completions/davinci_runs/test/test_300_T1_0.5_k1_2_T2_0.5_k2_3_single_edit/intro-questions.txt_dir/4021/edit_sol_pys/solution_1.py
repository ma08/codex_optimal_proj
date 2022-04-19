

import sys

def main():
	a = int(sys.stdin.readline().rstrip())
	b = int(sys.stdin.readline().rstrip())
	if a > b:
		print(a)
	else:
		print(b)


if __name__ == "__main__":
	main()

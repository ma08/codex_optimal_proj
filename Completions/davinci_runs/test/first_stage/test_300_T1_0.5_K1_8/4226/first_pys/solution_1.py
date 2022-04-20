

import sys

def main():
	x, y = map(int, sys.stdin.readline().split())
	if y % 2 == 0:
		if x == (y / 2):
			print("Yes")
		else:
			print("No")
	else:
		print("No")

if __name__ == "__main__":
	main()
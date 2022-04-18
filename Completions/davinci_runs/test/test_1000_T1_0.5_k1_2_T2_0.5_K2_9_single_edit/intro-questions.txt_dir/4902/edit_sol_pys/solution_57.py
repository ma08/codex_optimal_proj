import math
import sys

def main():
	n = int(raw_input())
	arr = map(int, raw_input().split())
	s = 0
	for i in arr:
		s += i
	print math.ceil(float(s)/float(n))

if __name__ == "__main__":
	main()

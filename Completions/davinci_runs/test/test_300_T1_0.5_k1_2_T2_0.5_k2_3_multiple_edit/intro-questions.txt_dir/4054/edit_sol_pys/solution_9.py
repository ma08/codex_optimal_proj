#!/usr/bin/python3

import sys

def main():
	# Read input
	a = [int(x) for x in sys.stdin.readline().split()] # TODO: Fix this line

	# Compute and print answer
	print(min(a)) # TODO: Fix this line

if __name__ == '__main__':
	main()

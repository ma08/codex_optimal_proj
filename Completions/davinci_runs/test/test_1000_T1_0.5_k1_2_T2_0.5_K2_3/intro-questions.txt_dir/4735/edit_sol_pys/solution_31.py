#!/usr/bin/env python3

import sys

def is_launch_window_open(year):
	if year % 26 == 2:
		print("yes")
	else:
		print("no")

def main():
	year = int(sys.stdin.readline())
	is_launch_window_open(year)

if __name__ == "__main__":
	main()

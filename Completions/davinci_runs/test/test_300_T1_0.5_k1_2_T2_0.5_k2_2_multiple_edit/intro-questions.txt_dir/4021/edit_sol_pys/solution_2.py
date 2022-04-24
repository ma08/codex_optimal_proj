#!/usr/bin/env python3

import sys
import os

def main():
	a = sys.stdin.readline()
	b = os.path.basename(a)
	print(b)


if __name__ == "__main__":
	main()

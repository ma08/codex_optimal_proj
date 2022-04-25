

import sys, re

def solve(expr):
	result = eval(expr)
	print(result)
	return result

def bf_solve(expr, bf):
	result = eval(expr, bf)
	# print(result)
	return result

def encode(expr):
	result = bf_solve(expr, bf)
	print(result)

def main():
	expr = sys.stdin.readline().strip()
	# print(expr)
	solve(expr)
	# encode(expr)

if __name__ == '__main__':
	main()

#http://codeforces.com/problemset/problem/1210/A

import sys

def main():

	s = sys.stdin.readline().strip()
	n = int(sys.stdin.readline().strip())

	if n % 2 == 0:
		if s[:n//2] == s[n//2:]:
			print(n//2)
		else:
			print(n)
	else:
		if s[:n//2] == s[n//2+1:]:
			print(n//2)
		else:
			print(n)

main()

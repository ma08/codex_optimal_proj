

import sys

def main():
	n = int(input().strip())
	a = list(map(int,input().strip().split(' ')))
	b = [0]*n
	for i in range(n):
		b[i] = a.count(i+1)
	if (b[0] == n):
		print("NO")
		sys.exit(0)
	for i in range(n-1):
		if (b[i+1] == n and b[i] == 1):
			print("NO")
			sys.exit(0)
	print("YES")

if __name__ == '__main__':
	main()

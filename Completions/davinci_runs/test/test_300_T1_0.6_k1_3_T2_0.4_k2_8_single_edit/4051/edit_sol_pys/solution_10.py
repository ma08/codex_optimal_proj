

import sys

def main():
	n = int(input().strip())
	a = list(map(int,input().strip().split(' ')))
	b = [0]*(n+1)
	for i in range(n):
		b[a[i]] = b[a[i]] + 1
	if (b[1] == n or b[n] == n):
		print("NO")
		sys.exit(0)
	for i in range(1,n-1):
		if (b[i+1] == n or (b[i+1] == 1 and b[i+2] == n)):
			print("NO")
			sys.exit(0)
	print("YES")

if __name__ == '__main__':
	main()

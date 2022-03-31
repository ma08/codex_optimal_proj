

import sys

def main():
	n = int(sys.stdin.readline())
	q = list(map(int, sys.stdin.readline().split()))

	if n == 2:
		print(1,1+q[0])
		return

	p = [0]*n
	p[0] = q[0]
	p[1] = q[1]+p[0]
	for i in range(2,n):
		p[i] = q[i]+p[i-1]
		if p[i] < p[i-1] or p[i] < 1:
			print(-1)
			return
	print(*p)

if __name__ == "__main__":
	main()
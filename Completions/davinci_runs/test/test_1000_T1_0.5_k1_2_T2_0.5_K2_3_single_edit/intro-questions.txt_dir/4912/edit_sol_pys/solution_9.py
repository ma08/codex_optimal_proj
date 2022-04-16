
#!/usr/bin/env python
import sys

def main():
	h,w,n = map(int,sys.stdin.readline().split())
	bricks = map(int,sys.stdin.readline().split())
	bricks.sort()
	sum = 0
	i = 0
	for i in range(n):
		sum += bricks[i]
		if sum >= w:
			h -= 1
			sum = 0
			i -= 1
		if h == 0:
			print "YES"
			break
	if h != 0:
		print "NO"

if __name__ == "__main__":
	main()

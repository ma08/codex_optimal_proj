

import sys
import math

def solve(q):
	for k in q:
		if k == 1:
			yield 1
		elif k == 2:
			yield 1
		elif k == 3:
			yield 2
		else:
			# find the block
			block = math.floor(math.sqrt(k))
			if block == math.sqrt(k):
				block -= 1
			# find the element in the block
			el = k - block * (block + 1)
			# find the digit
			digit = str(block)[el - 1]
			yield int(digit)

if __name__ == '__main__':
	q = int(sys.stdin.readline().strip())
	q = [int(sys.stdin.readline().strip()) for _ in range(q)]
	ans = solve(q)
	print(*ans,sep='\n')
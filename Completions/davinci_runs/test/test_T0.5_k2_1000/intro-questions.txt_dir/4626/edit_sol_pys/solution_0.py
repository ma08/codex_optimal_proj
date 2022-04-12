
# SOLUTION
import sys

def min_pairwise_distance(a, b, c):
	return min(abs(a-b)+abs(b-c)+abs(c-a), abs(a-b-1)+abs(b-c-1)+abs(c-a-1), abs(a-b+1)+abs(b-c+1)+abs(c-a+1), abs(a-b-1)+abs(b-c)+abs(c-a-1), abs(a-b+1)+abs(b-c)+abs(c-a+1), abs(a-b)+abs(b-c-1)+abs(c-a-1), abs(a-b)+abs(b-c+1)+abs(c-a+1))

q = int(sys.stdin.readline().strip())

for i in range(q):
	a, b, c = map(int, sys.stdin.readline().strip().split())
	print(min_pairwise_distance(a, b, c))

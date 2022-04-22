
import sys
N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
B = sorted(A)
for a in A:
    print(B.index(a)+1)

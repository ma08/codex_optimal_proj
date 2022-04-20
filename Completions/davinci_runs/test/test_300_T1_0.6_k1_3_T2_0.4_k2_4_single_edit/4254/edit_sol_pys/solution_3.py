
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

print(max(A) - min(A))

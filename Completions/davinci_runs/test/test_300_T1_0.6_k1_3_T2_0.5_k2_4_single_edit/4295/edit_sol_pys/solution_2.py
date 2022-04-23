
from sys import stdin
# Read from standard input
N, K = map(int, stdin.readline().split())
# If N is even and K is odd, Aoki can always make N=0
if N % 2 == 0 and K % 2 == 1:
    print(0)
# Else, the minimum value is N modulo K
else:
    print(N % K)

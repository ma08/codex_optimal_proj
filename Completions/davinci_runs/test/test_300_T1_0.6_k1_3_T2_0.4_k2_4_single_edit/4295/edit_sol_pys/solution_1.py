

from sys import stdin

# Read from standard input
N, K = map(int, stdin.readline().split())

# If N is odd and K is even, Aoki can always make N=0
if N % 2 == 1 and K % 2 == 0:
    print(0)
# Else, the minimum value is N modulo K
else:
    print(N % K)

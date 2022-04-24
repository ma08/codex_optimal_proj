

from sys import stdin

N, K = map(int, stdin.readline().split())

if N % 2 == 0 and K % 2 == 1:
    print(0)
else:
    print(N % K)

import sys


n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(M):
    P, X = P_X[i]
    print(sum(T) - T[P-1] + X)

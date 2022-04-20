import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
if N == M:
    print("Yes")
else:
    print("No")

import sys
sys.setrecursionlimit(10 ** 7)


if sum(a) // k < 2:
    print(ans)
else:
    print(ans + sum(a) // k - 1)

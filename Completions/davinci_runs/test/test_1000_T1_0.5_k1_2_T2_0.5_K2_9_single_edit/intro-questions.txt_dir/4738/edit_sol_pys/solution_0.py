import sys
sys.setrecursionlimit(1000000000)


def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

n = int(input())
print(f(n))

import sys


def f(n, k):
    if n % k == 0:
        return 'YES'
    if k % 2 == 0:
        if n % 2 == 0:
            return 'NO'
        else:
            return 'YES'
    else:
        if n % 2 == 0:
            return 'YES'
        else:
            return 'NO'


t = int(sys.stdin.readline())
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    print(f(n, k))

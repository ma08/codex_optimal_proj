

from collections import Counter
from math import log

def is_good(a):
    a = sorted(a)
    n = len(a)
    s = 0
    for i in range(n):
        if a[i] != 0:
            s += log(a[i], 2)
            if s % 1 == 0:
                return True
    return False

def solve(a):
    n = len(a)
    if is_good(a):
        return 0
    for i in range(1, n+1):
        if is_good(a[:i]):
            return n - i
    return n

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

if __name__ == "__main__":
    main()
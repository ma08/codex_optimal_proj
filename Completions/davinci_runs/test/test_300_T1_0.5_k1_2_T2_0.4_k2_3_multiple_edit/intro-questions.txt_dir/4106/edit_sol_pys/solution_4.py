

from sys import stdin
from itertools import accumulate

def solve(n, k, x, a):
    if x < k:
        return -1
    elif k == 1:
        return sum(a)
    else:
        acc = [0] + list(accumulate(a))
        prefix = acc[:n-k+1]
        suffix = acc[n-k+1:] + [0]
        max_suffix = [0] * (n-k+2)
        for i in range(n-k, -1, -1):
            max_suffix[i] = max(max_suffix[i+1], suffix[i])
        res = 0
        for i in range(n-k+1):
            res = max(res, prefix[i]+max_suffix[i])
        return res

def main():
    n, k, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, x, a))

if __name__ == "__main__":
    main()



from sys import stdin
from itertools import accumulate

def solve(n, k, x, a):
    if x < k:
        return 0
    elif k == 1:
        return sum(a)
    else:
        acc = list(accumulate(a[:k]))
        max_suffix = [0] * (k+1)
        for i in range(k-1, -1, -1):
            max_suffix[i] = max(max_suffix[i+1], acc[i])
        prefix = [0] * (k+1)
        for i in range(k):
            prefix[i+1] = max(prefix[i], acc[i])
        res = x * sum(a[:k])
        for i in range(k, n):
            res = max(res, prefix[i-k+1]+max_suffix[i-k+1]+(x-1)*a[i])
        return res % (10**9+7)

def main():
    n, k, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, x, a))

if __name__ == "__main__":
    main()

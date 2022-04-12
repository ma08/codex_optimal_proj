
from sys import stdin
from itertools import accumulate

def solve(n, k, x, a):
    if x < k - 1:
        return -1
    elif k == 1:
        return sum(a)
    else:
        acc = list(accumulate(a))
        prefix = [0] + acc[:n - k + 1]
        suffix = acc[k - 1:] + [0]
        max_suffix = [0] * (n - k + 1)
        for i in range(n - k, -1, -1):
            max_suffix[i] = max(max_suffix[i + 1], suffix[i])
        res = 0
        for i in range(n - k + 1):
            res = max(res, prefix[i] + max_suffix[i + 1])
        return res

def main():
    n, k, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, x, a))

if __name__ == "__main__":
    main()

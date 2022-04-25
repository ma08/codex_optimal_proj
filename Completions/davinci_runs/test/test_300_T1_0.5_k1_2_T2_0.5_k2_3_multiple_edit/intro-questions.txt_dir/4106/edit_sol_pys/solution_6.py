
from sys import stdin
from itertools import accumulate

def solve(n, k, x, a):
    if x < k:
        return -1
    elif k == 1:
        return sum(a)
    else:
        acc = list(accumulate(a))
        prefix = [0] + acc[:n-k+1] # prefix sum
        suffix = acc[k-1:] + [0] # suffix sum
        max_suffix = [0] # max suffix sum
        for i in range(n-k, -1, -1):
            max_suffix.append(max(max_suffix[-1], suffix[i]))
        max_suffix = max_suffix[::-1]
        res = 0
        for i in range(n-k+1):
            res = max(res, prefix[i]+max_suffix[i+1])
        return res

def main():
    n, k, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, x, a))

if __name__ == "__main__":
    main()

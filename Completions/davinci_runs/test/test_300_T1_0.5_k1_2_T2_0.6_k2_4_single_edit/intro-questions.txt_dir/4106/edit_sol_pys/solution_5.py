
from sys import stdin
from itertools import accumulate

def main():
    n, k, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    if x < k:
        print(-1)
        return
    elif k == 1:
        print(sum(a))
        return
    acc = list(accumulate(a))
    prefix = [0] + acc[:n-k+1]
    suffix = acc[k-1:] + [0]
    max_suffix = [0]
    for i in range(n-k, -1, -1):
        max_suffix.append(max(max_suffix[-1], suffix[i]))
    max_suffix = max_suffix[::-1]
    res = 0
    for i in range(n-k+1):
        res = max(res, prefix[i]+max_suffix[i+1])
    print(res)


if __name__ == "__main__":
    main()

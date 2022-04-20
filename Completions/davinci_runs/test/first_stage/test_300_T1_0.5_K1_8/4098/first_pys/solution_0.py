

import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    a = sorted(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(n):
        if a[i] - a[0] <= 5:
            ans = max(ans, i+1)
    print(min(k, ans))
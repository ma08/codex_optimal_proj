

import bisect

def solve(n, k, a):
    a.sort()
    if k == 0:
        return 1
    elif k == n:
        return a[-1]
    else:
        l = 0
        r = n - 1
        while l < r:
            m = (l + r) // 2
            if k <= m:
                r = m
            else:
                l = m + 1
        return a[l]


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
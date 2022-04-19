

import sys

def solve(n, m, a):
    a.sort()
    ans = 0
    for i in range(m):
        if a[i] < 0:
            ans += a[i]

    print(-ans)

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    solve(n, m, a)

if __name__ == '__main__':
    main()

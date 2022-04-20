

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    if a[0] > m:
        print(-1)
        return
    if a[0] == m:
        print(1)
        return
    for i in range(1, n):
        a[i] = max(0, a[i] - i)
    a.sort()
    if a[0] == 0:
        print(-1)
        return
    if a[0] == m:
        print(1)
        return
    ans = 0
    while m > 0:
        ans += 1
        m -= a[0]
    print(ans)

if __name__ == '__main__':
    main()

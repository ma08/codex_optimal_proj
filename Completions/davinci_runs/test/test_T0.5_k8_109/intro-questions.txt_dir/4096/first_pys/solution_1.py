

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    if sum(a) < m:
        print(-1)
        return
    if m <= n:
        print(1)
        return
    cur = 0
    for i in range(n):
        cur += a[i] - i
        if cur >= m:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()
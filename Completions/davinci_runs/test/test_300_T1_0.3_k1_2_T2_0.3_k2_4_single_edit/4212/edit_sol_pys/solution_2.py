

import sys

def main():
    n, m, q = map(int, sys.stdin.readline().split())
    a = [0] * (m + 1)
    for _ in range(q):
        ai, bi, ci, di = map(int, sys.stdin.readline().split())
        a[ai - 1] += di
        a[bi] -= di # ai <= bi
    for i in range(1, m + 1):
        a[i] += a[i - 1]
    print(max(a))

if __name__ == '__main__':
    main()


import sys

def main():
    n, m, q = map(int, sys.stdin.readline().split())
    a = [0] * (n + 1)
    for _ in range(q):
        ai, bi, ci, di = map(int, sys.stdin.readline().split())
        a[ai] += di
        a[bi] -= di
    for i in range(1, n):
        a[i + 1] += a[i]
    print(max(a))

if __name__ == '__main__':
    main()

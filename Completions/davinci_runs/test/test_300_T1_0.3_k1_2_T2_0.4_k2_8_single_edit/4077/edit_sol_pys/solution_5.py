
import sys


def median(l, r):
    return (l + r) // 2


def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, input().split()))

    a.sort()

    count = 0
    for i in range(n):
        for j in range(i, n):
            if median(a[i], a[j]) == m:
                count += 1

    print(count)

if __name__ == "__main__":
    main()


import sys

def median(a, l, r):
    return a[(l + r) // 2]

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    a.sort()

    count = 0
    for i in range(n):
        for j in range(i, n):
            if median(a, i, j) == m:
                count += 1

    print(count)

if __name__ == "__main__":
    main()

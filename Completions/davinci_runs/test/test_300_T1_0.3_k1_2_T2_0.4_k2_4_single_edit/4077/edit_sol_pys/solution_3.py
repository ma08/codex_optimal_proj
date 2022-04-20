
import sys


def median(arr, left, right):
    if (right - left) % 2 == 0:
        return arr[(left + right) // 2]
    else:
        return arr[(left + right) // 2 + 1]


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()

    count = 0
    for i in range(n):
        for j in range(i, n):
            if median(arr, i, j) == m:
                count += 1

    print(count)

if __name__ == "__main__":
    main()

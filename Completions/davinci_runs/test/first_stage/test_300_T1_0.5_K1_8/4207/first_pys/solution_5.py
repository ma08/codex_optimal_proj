


import math


def solve(a, b):
    n = len(a)

    max_zeroes = 0
    for i in range(n):
        if a[i] == 0:
            if b[i] == 0:
                max_zeroes += 1
            continue

        d = -b[i] / a[i]
        zeroes = 0
        for j in range(n):
            if b[j] + a[j] * d == 0:
                zeroes += 1
        max_zeroes = max(max_zeroes, zeroes)

    return max_zeroes


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(a, b))


if __name__ == "__main__":
    main()
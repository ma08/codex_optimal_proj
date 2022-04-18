import math


def main():
    n, k = map(float, input().split())
    if k * (k + 1) / 2 <= n:
        print(int(math.ceil(n - k * (k + 1) / 2)))
    else:
        print(int(math.floor(2 * n / k - k / 2 - 1)))


if __name__ == '__main__':
    main()

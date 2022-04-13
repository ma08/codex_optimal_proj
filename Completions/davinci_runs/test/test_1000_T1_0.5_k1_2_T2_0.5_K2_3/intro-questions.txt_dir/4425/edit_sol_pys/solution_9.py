from math import ceil, floor



def main():
    n, k = map(float, input().split())
    if k * (k + 1) / 2 <= n:
        print(int(ceil(n - k * (k + 1) / 2)))
    else:
        print(int(floor(2 * n / k - k / 2 - 1)))


if __name__ == '__main__':
    main()

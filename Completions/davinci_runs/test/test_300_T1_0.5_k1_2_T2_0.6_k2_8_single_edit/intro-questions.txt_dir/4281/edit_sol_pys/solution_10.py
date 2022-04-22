import sys
sys.setrecursionlimit(10**7)


def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    print(nCr(n, k))


def nCr(n, r):
    if r == 0:
        return 1
    if n < r:
        return 0
    return nCr(n-1, r-1) * n / r


if __name__ == "__main__":
    main()

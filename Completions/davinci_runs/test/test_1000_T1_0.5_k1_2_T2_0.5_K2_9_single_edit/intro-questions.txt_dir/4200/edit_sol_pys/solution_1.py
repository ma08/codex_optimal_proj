import math


def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]

    ans = 0
    for i in range(n):
        ans += a[i] * (1 / 2 ** i)

    print(ans)


if __name__ == "__main__":
    main()

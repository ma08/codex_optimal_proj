
import math


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * max(0, min(k, n - i))
    print(ans)


if __name__ == '__main__':
    main()

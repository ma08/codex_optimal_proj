

import sys


def main():
    N = int(input())
    A, B, C, D = list(map(int, input().split()))

    ans = 0

    for n in range(N):
        a = n // (A + B)
        b = n // (C + D)
        ans = max(ans, n + a + b)

    print(ans)

if __name__ == "__main__":
    main()

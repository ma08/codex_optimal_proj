

import sys
import math


def main():
    N = int(input())
    ans = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            ans += N // i - 1
    print(ans)


if __name__ == "__main__":
    main()
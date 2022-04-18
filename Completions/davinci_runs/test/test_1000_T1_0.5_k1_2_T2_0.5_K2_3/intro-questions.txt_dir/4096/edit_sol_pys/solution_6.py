

import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if a[-1] < m:
        if m % a[-1] == 0:
            print(math.ceil(m / a[-1]))
            return

    for i in range(n):
        m -= a[i]
        if m <= 0:
            print(i + 1)
            return


    print(-1) 


if __name__ == "__main__":
    main()

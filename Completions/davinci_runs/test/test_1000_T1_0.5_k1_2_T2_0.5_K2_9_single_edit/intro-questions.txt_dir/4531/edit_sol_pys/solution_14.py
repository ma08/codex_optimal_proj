import math
import sys

sys.setrecursionlimit(10 ** 6)


def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    cnt = 0
    for i in range(n):
        if a[i] % 2 == 0:
            cnt += 1

    if cnt % 2 == 0:
        print(n - cnt)
    else:
        print(n - cnt + 1)




if __name__ == "__main__":
    main()

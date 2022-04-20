
import math
import sys

def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort(reverse=True)

    sum_a = sum(a)

    if sum_a % 10 != 0:
        print(sum_a)
    else:
        for i in range(n):
            if (sum_a - a[i]) % 10 != 0:
                print(sum_a - a[i])
                return

        print(0)


if __name__ == "__main__":
    main()

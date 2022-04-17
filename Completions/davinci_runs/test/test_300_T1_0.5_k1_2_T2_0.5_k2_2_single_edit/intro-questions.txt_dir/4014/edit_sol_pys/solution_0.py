
import re
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    c = 0
    x = 0
    for i in range(n):
        if a[i] == 0:
            c += 1
        else:
            x += c // 2
            c = 0
    x += c // 2

    print(x)


if __name__ == "__main__":
    main()

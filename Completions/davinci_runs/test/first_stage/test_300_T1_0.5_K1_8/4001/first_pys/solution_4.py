

import sys

def main():
    n = int(input())
    divisors = list(map(int, input().split()))

    x = 1
    y = 1

    for i in range(n):
        if i > 0 and divisors[i] == divisors[i-1]:
            x *= divisors[i]
        elif i > 0 and divisors[i] != divisors[i-1]:
            y *= divisors[i]
        else:
            x *= divisors[i]

    print("{} {}".format(x, y))

if __name__ == '__main__':
    main()
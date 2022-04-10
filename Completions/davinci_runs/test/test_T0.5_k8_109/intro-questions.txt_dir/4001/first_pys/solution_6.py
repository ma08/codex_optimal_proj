

import sys

def main():
    n = int(sys.stdin.readline())
    divisors = [int(x) for x in sys.stdin.readline().split()]

    x = 1
    y = 1
    for d in divisors:
        if divisors.count(d) == 1:
            x *= d
        else:
            y *= d

    print(x, y)


if __name__ == "__main__":
    main()
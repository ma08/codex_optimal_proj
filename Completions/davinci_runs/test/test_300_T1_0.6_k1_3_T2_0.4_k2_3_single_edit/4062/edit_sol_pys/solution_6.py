

import sys

def max_product(a, b, c, d, e, f):
    max_prod = 0.0

    for i in range(a, b + 1):
        for j in range(c, d + 1):
            max_prod = max(max_prod, (i * j) / (e * f))
    
    return max_prod


def main():
    a, b, c, d, e, f = map(int, sys.stdin.readline().split(' '))
    print(max_product(a, b, c, d, e, f))


if __name__ == "__main__":
    main()

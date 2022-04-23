

import sys

def max_product(x, y, z, w):
    max_prod = 0

    for i in range(x, y + 1):
        for j in range(z, w + 1):
            max_prod = max(max_prod, i * j)
    
    return max_prod


def main():
    x, y, z, w = map(int, sys.stdin.readline().split(' '))
    print(max_product(x, y, z, w))


if __name__ == "__main__":
    main()

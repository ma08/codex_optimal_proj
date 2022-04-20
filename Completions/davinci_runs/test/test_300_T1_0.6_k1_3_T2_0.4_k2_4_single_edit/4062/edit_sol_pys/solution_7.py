import sys
import math



def max_product(n, a, b, c, d):
    max_prod = -math.inf

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            max_prod = max(max_prod, i * j)
    
    return max_prod


def main():
    n, a, b, c, d = map(int, sys.stdin.readline().split(' '))
    print(max_product(n, a, b, c, d))


if __name__ == "__main__":
    main()

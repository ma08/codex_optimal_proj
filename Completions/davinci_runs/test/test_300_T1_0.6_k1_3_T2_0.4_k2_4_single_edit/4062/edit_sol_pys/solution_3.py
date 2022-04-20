
import sys

def max_product(a, b, c, d):
    max_prod = 0
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            max_prod = max(max_prod, i * j)
    
    return max_prod


def main():
    a, b, c, d = map(int, sys.stdin.readline().split(' '))
    print(max_product(a, b, c, d))

if __name__ == "__main__":
    main()

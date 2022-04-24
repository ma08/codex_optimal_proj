

import sys

def max_product(a, b, c, d, k):
    max_prod = 0,
    count = 0

    for i in range(a, b + 1):
        for j in range(c, d + 1):
            if count < k:
                max_prod = max(max_prod, i * j)
                count += 1
            else:
                break
    return max_prod, count


def main():
    a, b, c, d, k = map(int, sys.stdin.readline().split(' '))
    print(max_product(a, b, c, d, k))


if __name__ == "__main__":
    main()

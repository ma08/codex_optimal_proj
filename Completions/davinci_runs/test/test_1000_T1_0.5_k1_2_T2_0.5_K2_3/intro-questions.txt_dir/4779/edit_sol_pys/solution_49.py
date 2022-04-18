
import math


def main():
    n = int(input())
    inputs = [int(i) for i in input().split()]
    inputs.sort(reverse=True)
    max_val = 0
    for i, num in enumerate(inputs):
        max_val = max(max_val, num * (i + 1))
    print(max_val % (10 ** 9 + 7))


if __name__ == '__main__':
    main()

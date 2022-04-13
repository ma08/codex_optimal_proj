
import math


def main():
    n = int(input())
    input_list = [int(i) for i in input().split()]
    input_list.sort(reverse=True)
    max_val = 0
    for i, num in enumerate(input_list):
        max_val = max(max_val, num * (i + 1))
    print(max_val % (10 ** 9 + 7))


if __name__ == '__main__':
    main()

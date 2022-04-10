

import sys

def main():
    n, x, y = [int(i) for i in sys.stdin.readline().split()]
    number = sys.stdin.readline().strip()
    print(min_operations_to_get_remainder(number, x, y))


def min_operations_to_get_remainder(number, x, y):
    """
    :param number: decimal number without leading zeros, only 0 or 1 digits
    :param x: x
    :param y: y
    :return: minimum number of operations required to get the number having remainder 10^y modulo 10^x
    """
    remainder = int(number[-x:], 2)
    remainder_to_get = 10 ** y
    if remainder == remainder_to_get:
        return 0
    elif remainder < remainder_to_get:
        if remainder_to_get - remainder < remainder_to_get // 2:
            return remainder_to_get - remainder
        else:
            return remainder_to_get - remainder - remainder_to_get // 2
    else:
        if remainder - remainder_to_get < remainder_to_get // 2:
            return remainder - remainder_to_get
        else:
            return remainder - remainder_to_get - remainder_to_get // 2


if __name__ == "__main__":
    main()
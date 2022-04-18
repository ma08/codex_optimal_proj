
import math


def main():
    # a = float(input())
    a = 4.024922
    a_ceil = math.ceil(a)
    a_floor = math.floor(a)
    a_round = round(a)

    a_ceil_10 = a_ceil * 10
    a_floor_10 = a_floor * 10
    a_round_10 = a_round * 10

    a_ceil_10_remainder = a_ceil_10 % a
    a_floor_10_remainder = a_floor_10 % a
    a_round_10_remainder = a_round_10 % a

    if a_ceil_10_remainder < a_floor_10_remainder:
        print(a_ceil, 10)
    elif a_floor_10_remainder < a_round_10_remainder:
        print(a_floor, 10)
    else:
        print(a_round, 10)


if __name__ == '__main__':
    main()

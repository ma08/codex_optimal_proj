import math


def main():
    # a = float(input())
    a = 4.02492235
    a_ceil = math.ceil(a)
    a_floor = math.floor(a)
    a_round = round(a)

    a_ceil_10 = a_ceil * 100
    a_floor_10 = a_floor * 100
    a_round_10 = a_round * 100

    a_ceil_10_remainder = a_ceil_10 % 100
    a_floor_10_remainder = a_floor_10 % 100
    a_round_10_remainder = a_round_10 % 100

    print("a_ceil_10_remainder: ", a_ceil_10_remainder)
    print("a_floor_10_remainder: ", a_floor_10_remainder)
    print("a_round_10_remainder: ", a_round_10_remainder)

    if a_ceil_10_remainder < a_floor_10_remainder and a_ceil_10_remainder < a_round_10_remainder:
        print(a_ceil, 100)
    elif a_floor_10_remainder < a_ceil_10_remainder and a_floor_10_remainder < a_round_10_remainder:
        print(a_floor, 100)
    else:
        print(a_round, 100)


if __name__ == '__main__':
    main()

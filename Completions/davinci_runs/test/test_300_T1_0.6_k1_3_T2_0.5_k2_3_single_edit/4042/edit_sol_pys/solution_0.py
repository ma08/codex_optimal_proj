


def main():
    # a = float(input())
    a = 4.024922
    a_ceil = math.ceil(a)  # 5
    a_floor = math.floor(a)  # 4
    a_round = round(a)

    a_ceil_10 = a_ceil * 10  # 50
    a_floor_10 = a_floor * 10  # 40
    a_round_10 = a_round * 10  # 40

    a_ceil_10_remainder = a_ceil_10 % a  # 5.024922
    a_floor_10_remainder = a_floor_10 % a  # 0.975078
    a_round_10_remainder = a_round_10 % a  # 0.975078

    if a_ceil_10_remainder < a_floor_10_remainder:
        print(a_ceil, 10)  # 5 10
    elif a_floor_10_remainder < a_round_10_remainder:
        print(a_floor, 10)  # 4 10
    else:
        print(a_round, 10)  # 4 10


if __name__ == '__main__':
    main()



# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 087
# Problem A


def count_500_yen_coins(x):
    return int(x / 500)


def count_100_yen_coins(x):
    return int(x / 100)


def count_50_yen_coins(x):
    return int(x / 50)


if __name__ == '__main__':
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    result = 0

    for i in range(0, A + 1):
        for j in range(0, B + 1):
            for k in range(0, C + 1):
                if 500 * i + 100 * j + 50 * k == X:
                    result += 1

    print(result)

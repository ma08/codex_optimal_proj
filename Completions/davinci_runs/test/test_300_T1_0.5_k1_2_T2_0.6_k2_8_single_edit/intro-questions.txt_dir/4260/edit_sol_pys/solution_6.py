

from __future__ import print_function


def read_line():
    return input()


def read_ints():
    return list(map(int, read_line().split(' ')))


def read_floats():
    return list(map(float, read_line().split(' ')))


def main():
    T, X = read_ints()
    print(T/X)


if __name__ == '__main__':
    main()

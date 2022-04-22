

# https://qiita.com/kazetof/items/1d902c7b2a2af0d7f8b8
import sys


def read_ints(sys.stdin.readline):
    return list(map(int, sys.stdin.readline().split(' ')))


def read_floats(sys.stdin.readline):
    return list(map(float, sys.stdin.readline().split(' ')))


def main():
    T, X = read_ints(sys.stdin.readline)
    print(T / X)


if __name__ == '__main__':
    main()

import math


def main():
    a, b = map(int, input().split())
    print(math.ceil((a + b) / 2))


if __name__ == '__main__':
    main()

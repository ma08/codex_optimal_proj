import math


def main():
    b, g = [int(x) for x in input().split()]
    print(math.ceil(b / g))

if __name__ == "__main__":
    main()

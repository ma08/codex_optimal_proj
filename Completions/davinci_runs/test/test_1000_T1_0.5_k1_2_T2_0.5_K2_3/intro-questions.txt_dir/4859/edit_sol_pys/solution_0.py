
import sys


def legs(b, d, c, le):
    if le < 0:
        return 0
    if b == 0 and d == 0 and c == 0:
        print("{} {} {}".format(b, d, c))
        return 1
    return legs(b - 1, d, c, le - b) + legs(b, d - 1, c, le - d) + legs(b, d, c - 1, le - c)


def main():
    data = sys.stdin.readline().split()
    b = int(data[0])
    d = int(data[1])
    c = int(data[2])
    le = int(data[3])
    print(legs(b, d, c, le))


if __name__ == "__main__":
    main()

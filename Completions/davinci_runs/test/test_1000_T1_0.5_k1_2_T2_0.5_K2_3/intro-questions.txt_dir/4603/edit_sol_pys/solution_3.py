
import sys

def calc_min_fare(a, b, c, d):
    return min(a, b) + min(c, d)

def main():
    a = int(sys.stdin.readline())  # noqa
    b = int(sys.stdin.readline())  # noqa
    c = int(sys.stdin.readline())  # noqa
    d = int(sys.stdin.readline())  # noqa
    print(calc_min_fare(a, b, c, d))

if __name__ == '__main__':
    main()

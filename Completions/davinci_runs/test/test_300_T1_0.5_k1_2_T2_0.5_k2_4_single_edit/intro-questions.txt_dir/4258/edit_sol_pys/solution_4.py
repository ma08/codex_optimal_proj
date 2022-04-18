import sys


def main():
    A, B, T = map(int, input().split())
    sys.stdout.write(str(B * (T // A + 1)))


if __name__ == '__main__':
    main()

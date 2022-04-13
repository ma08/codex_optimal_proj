
from sys import stdin


def main():
    x1, y1, x2, y2 = map(int, stdin.readline().strip().split())
    if x1 == x2 or y1 == y2:
        print(x1, y1, x2, y2)
    else:
        print('-1')


if __name__ == '__main__':
    main()

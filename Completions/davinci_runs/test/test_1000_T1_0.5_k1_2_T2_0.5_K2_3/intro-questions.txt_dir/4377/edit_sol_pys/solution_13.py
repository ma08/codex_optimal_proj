
from sys import stdin

def main():
    x1, y1, x2, y2 = [int(x) for x in stdin.readline().split()]
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        print(x1 + abs(y2 - y1), y1, x2 + abs(y2 - y1), y2)
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        print(x1, y1 + abs(x2 - x1), x2, y2 + abs(x2 - x1))
    else:
        print('-1')


if __name__ == '__main__':
    main()


from math import sqrt


def main():
    x, y, x1, y1, x2, y2 = map(int, input().split())
    if x <= x1:
        if y <= y1:
            print(sqrt((x1 - x) ** 2 + (y1 - y) ** 2))
        elif y >= y2:
            print(sqrt((x1 - x) ** 2 + (y2 - y) ** 2))
        else:
            print(x1 - x)
    elif x >= x2:
        if y <= y1:
            print(sqrt((x2 - x) ** 2 + (y1 - y) ** 2))
        elif y >= y2:
            print(sqrt((x2 - x) ** 2 + (y2 - y) ** 2))
        else:
            print(x - x2)
    else:
        if y <= y1:
            print(y1 - y)
        else:
            print(y - y2)


if __name__ == "__main__":
    main()


import math


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def main():
    abc = input().split()
    a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

    if a >= b and a >= c:
        if b >= c:
            print(triangle_area(a, b, c))
        else:
            print(triangle_area(a, c, b))
    elif b >= a and b >= c:
        if a >= c:
            print(triangle_area(b, a, c))
        else:
            print(triangle_area(b, c, a))
    else:
        if a >= b:
            print(triangle_area(c, a, b))
        else:
            print(triangle_area(c, b, a))


if __name__ == '__main__':
    main()

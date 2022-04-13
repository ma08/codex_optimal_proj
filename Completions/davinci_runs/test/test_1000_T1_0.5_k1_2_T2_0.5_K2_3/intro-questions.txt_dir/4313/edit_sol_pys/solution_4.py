

import math
import sys


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    D = b**2 - 4*a*c

    if D < 0:
        print("No roots")
    elif D == 0:
        x = -b / (2*a)
        print("One root:", x)
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("Two roots:", x1, x2)


if __name__ == '__main__':
    main()

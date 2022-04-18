
import sys
import math


def main(file):
    with open(file, 'r') as f:
        r, c = f.readline().strip().split()
        r = float(r)
        c = float(c)

        area = math.pi * r**2
        area_of_crust = math.pi * (r-c)**2

        print(round((area_of_crust/area)*100, 10))


if __name__ == '__main__':
    main(sys.argv[1])

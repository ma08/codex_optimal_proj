
import sys
import math

def main(pfile):
    with open(pfile, 'r') as f:
        r, c = [float(x) for x in f.readline().strip().split()]
        area = math.pi * (r**2)
        area_of_crust = math.pi * ((r - c)**2)

        print(round((area_of_crust / area) * 100, 10))

if __name__ == '__main__':
    main(sys.argv[1])

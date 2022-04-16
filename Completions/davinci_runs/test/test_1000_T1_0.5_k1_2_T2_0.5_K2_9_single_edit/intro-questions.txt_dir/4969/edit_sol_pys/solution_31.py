

import sys
import math

def main(pfile):
    with open(pfile, 'r') as pf:
        rc = pf.readline().strip().split()
        r = float(rc[0])
        c = float(rc[1])

        area = math.pi * (r**2)
        area_of_crust = math.pi * ((r-c)**2)

        print(round((area_of_crust / area) * 100, 6))

if __name__ == '__main__':
    main(sys.argv[1])

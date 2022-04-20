

import sys
from functools import reduce
from math import gcd
from operator import mul

def main():
    # read input
    A, B = map(int, sys.stdin.readline().split())

    # calculate LCM(A, B)
    LCM = reduce(mul, [A, B], 1) // gcd(A, B)

    # print result
    print(LCM)

if __name__ == "__main__":
    main()

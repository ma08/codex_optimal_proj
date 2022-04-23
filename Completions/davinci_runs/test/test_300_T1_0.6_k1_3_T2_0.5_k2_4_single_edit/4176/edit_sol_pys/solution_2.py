

"""
-----Notes-----

We can say that the LCM of A and B is the minimum number of snack pieces that can be evenly distributed to the guests in both of the cases.

LCM(A, B) = A × B ÷ GCD(A, B)
"""

import sys
from functools import reduce
from math import gcd
from operator import mul

def main():
    # read input
    a, b = map(int, sys.stdin.readline().split())

    # calculate LCM(A, B)
    lcm = reduce(mul, [a, b], 1) // gcd(a, b)

    # print result
    print(LCM)

if __name__ == "__main__":
    main()

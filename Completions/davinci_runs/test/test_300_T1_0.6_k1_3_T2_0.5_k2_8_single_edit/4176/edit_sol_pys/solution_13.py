

"""
-----Notes-----

We can say that the LCM of A and B is the minimum number of snack pieces that can be evenly distributed to the guests in both of the cases.

LCM(A, B) = A × B ÷ GCD(A, B)
"""

import sys
from math import gcd

def main():
    # read input
    A, B = map(int, sys.stdin.readline().split())

    # calculate LCM(A, B)
    LCM = (A * B) // gcd(A, B)

    # print result
    print(LCM)

if __name__ == "__main__":
    main()

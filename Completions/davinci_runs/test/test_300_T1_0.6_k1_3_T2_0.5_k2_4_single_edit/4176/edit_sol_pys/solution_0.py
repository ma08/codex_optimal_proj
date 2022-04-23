
"""
Notes
-----

We can say that the LCM of A and B is the minimum number of snack pieces that can be evenly distributed to the guests in both of the cases.


Author
------
dbonadiman
LCM(A, B) = A × B ÷ GCD(A, B)
"""

import sys
from functools import reduce
from math import gcd
from operator import mul

def main():
    A, B = map(int, sys.stdin.readline().split())  # read input

    LCM = reduce(mul, [A, B], 1) // gcd(A, B)  # calculate LCM(A, B)

    print(LCM)  # print result

if __name__ == "__main__":
    main()


"""
-----Notes-----

We can say that the LCM of A and B is the minimum number of snack pieces that can be evenly distributed to the guests in both of the cases.


-----Input-----
1
2

-----Output-----
2

LCM(A, B) = A × B ÷ GCD(A, B)
"""

import sys
from functools import reduce
from math import gcd
from operator import mul

def main():
    A, B = map(int, input().split())

    # calculate LCM(A, B)
    LCM = reduce(mul, [A, B], 1) // gcd(A, B)

    # print result
    print(LCM)

if __name__ == "__main__":
    main()

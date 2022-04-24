
import sys
from functools import reduce
from math import gcd
from operator import mul

def main():
    # read input
    A, B = map(int, sys.stdin.readline().split())

    # calculate GCD(A, B)
    GCD = reduce(gcd, [A, B])

    # print result
    print(LCM)

if __name__ == "__main__":
    main()

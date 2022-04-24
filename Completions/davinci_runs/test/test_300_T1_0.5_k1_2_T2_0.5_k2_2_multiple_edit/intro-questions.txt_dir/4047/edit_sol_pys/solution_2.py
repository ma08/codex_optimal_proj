#!/usr/bin/env python3

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import sys

def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    gcd = math.gcd(n, m)
    lcm = n * m // gcd
    lcm_n = lcm // n
    lcm_m = lcm // m
    for i in range(gcd):
        if s[i*lcm_n] != t[i*lcm_m]:
            print(-1)
            sys.exit()
    print(lcm)

if __name__ == "__main__":
    main()

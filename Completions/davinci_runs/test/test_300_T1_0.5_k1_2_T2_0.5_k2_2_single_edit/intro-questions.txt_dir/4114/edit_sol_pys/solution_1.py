import os

import math
from decimal import Decimal, ROUND_HALF_UP
import sys

def main():
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(x + y // 2)

if __name__ == "__main__":
    main()

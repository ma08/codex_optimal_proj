

import sys
import math

def minDiff(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 1

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    print(minDiff(n))
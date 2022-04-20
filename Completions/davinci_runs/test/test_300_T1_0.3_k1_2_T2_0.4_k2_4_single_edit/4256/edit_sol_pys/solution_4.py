

import math
import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    print(math.ceil(N / K))



import math
import sys

K = int(sys.stdin.readline())

def main():
    cnt = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            for c in range(1, K+1):
                cnt += math.gcd(math.gcd(a, b), c)

def gcd3(a, b, c):
    return gcd(gcd(a, b), c)

def main():
    print(sum([gcd3(a, b, c) for a in range(1, K+1) for b in range(1, K+1) for c in range(1, K+1)]))

main()


import math
import sys

K = int(sys.stdin.readline())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def main():
    ans = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            for c in range(1, K + 1):
                ans += gcd(gcd(a, b), c)

    print(ans)

main()


import sys

K = int(sys.stdin.readline())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def gcd3(a, b, c, d):
    return gcd(gcd(a, b), gcd(c, d))

def main():
    print(sum([gcd3(a, b, c, d) for a in range(1, K+1) for b in range(1, K+1) for c in range(1, K+1) for d in range(1, K+1)]))

main()

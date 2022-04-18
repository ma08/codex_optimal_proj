import sys

K = int(sys.stdin.readline())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def main():
    print(sum([gcd(a, b) for a in range(1, K+1) for b in range(1, K+1)]))

main()

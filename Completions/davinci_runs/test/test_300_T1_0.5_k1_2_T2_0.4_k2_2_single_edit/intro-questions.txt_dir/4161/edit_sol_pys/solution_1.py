import sys
K = int(sys.stdin.readline())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def gcd3(a, b, c):
    return gcd(gcd(a, b), c)
def main():
    print(sum([gcd3(a, b, c) for a in range(1, K+1) for b in range(1, K+1) for c in range(1, K+1)]))

main()

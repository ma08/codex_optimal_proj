
import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    g = a[0] if n > 0 else 0
    for i in range(1, n if n > 0 else 1):
        g = gcd(g, a[i] if n > 0 else 0)
    print(g)

if __name__ == '__main__':
    main()

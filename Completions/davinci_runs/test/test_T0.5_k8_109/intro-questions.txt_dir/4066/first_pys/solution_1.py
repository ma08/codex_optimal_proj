

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    mi = sys.maxsize
    for i in range(n):
        for j in range(i + 1, n):
            l = lcm(a[i], a[j])
            if l < mi:
                mi = l
                m = (i, j)
    print(m[0] + 1, m[1] + 1)

main()
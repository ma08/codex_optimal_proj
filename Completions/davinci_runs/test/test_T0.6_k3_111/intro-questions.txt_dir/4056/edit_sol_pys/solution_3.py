from sys import stdin
from math import gcd

def solve(a):
    n = len(a)
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    return len(list(divisors(g)))

def divisors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            yield i
            if n // i != i:
                yield n // i
        i += 1

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    print(solve(a))

if __name__ == '__main__':
    main()

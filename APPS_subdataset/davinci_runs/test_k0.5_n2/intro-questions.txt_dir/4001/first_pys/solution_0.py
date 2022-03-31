

from functools import reduce
from collections import Counter

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a*b) // gcd(a, b)

def main():
    n = int(input())
    divisors = Counter(map(int, input().split()))
    x = reduce(lcm, divisors.keys())
    y = x
    for divisor, count in divisors.items():
        if count == 1:
            y = lcm(y, divisor)
    print(x, y)

if __name__ == "__main__":
    main()
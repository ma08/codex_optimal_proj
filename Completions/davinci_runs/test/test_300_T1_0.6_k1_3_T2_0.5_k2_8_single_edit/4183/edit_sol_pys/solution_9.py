

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    n = int(input())
    t = []
    for i in range(n):
        t.append(int(input()))

    ans = t[0]

    for i in t:
        ans = lcm(ans, i)

    print(ans)

if __name__ == "__main__":
    main()

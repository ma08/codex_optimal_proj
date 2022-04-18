# -*- coding: utf-8 -*-

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    k = int(input())

    ans = 0
    for a in range(1, k + 1):  # O(k)
        for b in range(1, k + 1):  # O(k)
            for c in range(1, k + 1):  # O(k)
                ans += gcd(a, b)  # O(logk)
                ans += gcd(b, c)  # O(logk)
                ans += gcd(c, a)  # O(logk)
                ans += gcd(gcd(a, b), c)  # O(logk)

    # O(k^2 logk)
    print(ans)

if __name__ == '__main__':
    main()

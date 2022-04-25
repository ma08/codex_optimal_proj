#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

def main():
    k = int(input())

    ans = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            for c in range(1, k + 1):
                ans += gcd(a, b)
                ans += gcd(b, c)
                ans += gcd(c, a)
                ans += gcd(gcd(a, b), c)
    print(ans)

if __name__ == '__main__':
    main()

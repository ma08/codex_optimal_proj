
# Solution for https://www.codechef.com/problems/CHN15A

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if a[0] == a[-1] else "NO")

if __name__ == "__main__":
    main()

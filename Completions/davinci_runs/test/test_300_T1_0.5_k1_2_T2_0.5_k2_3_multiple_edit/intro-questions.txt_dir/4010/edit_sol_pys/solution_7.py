
# Solution

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split())) # map() apply int() to every element in a list
        if a[0] == a[-1]: # a[-1] is the last element of a list
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

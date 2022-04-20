
# https://codeforces.com/problemset/problem/1328/A
# Solution

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    t = int(input()) # number of test cases
    for i in range(t): # loop through test cases
        n = int(input()) # number of elements in array
        a = list(map(int, input().split())) # array
        if a[0] == a[-1]: # if first and last elements are equal, print YES
            print("YES")
        else: # otherwise, print NO
            print("NO")

if __name__ == "__main__":
    main()

#!/usr/bin/python3
import sys
k, x = [int(i) for i in input().split()]

if (500 * k) >= x:
    print("Yes")
else:
    print("No")

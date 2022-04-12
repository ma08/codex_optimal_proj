#!/bin/python3
import re

if __name__ == '__main__':
    n = int(input())  # number of test cases
    for _ in range(n):  # loop through test cases
        s = input()  # get input
        print("YES" if re.match(r"^[789]\d{9}$", s) else "NO")  # print YES if match, else NO

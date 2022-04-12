#!/usr/bin/env python3

import sys

def main():
    n = read_int()
    nums = [read_int() for _ in range(n)]
    result = 0
    for num in nums:
        result += solve(num)
    print(result)

def solve(num):
    num_str = str(num)
    length = len(num_str)
    if length == 1:
        return int(num_str)
    else:
        return int(num_str[0])**(length-1) + int(num_str[1:])

def read_int():
    return int(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()

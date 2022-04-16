#!/usr/bin/env python3

import sys

def main():
    string = sys.stdin.readline().strip()
    dic = {}
    for char in string:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    count = 0
    odd = 0
    for key in dic:
        if dic[key] % 2 != 0:
            odd += 1
    if odd == 0:
        print(0)
    else:
        print(odd - 1)

if __name__ == '__main__':
    main()

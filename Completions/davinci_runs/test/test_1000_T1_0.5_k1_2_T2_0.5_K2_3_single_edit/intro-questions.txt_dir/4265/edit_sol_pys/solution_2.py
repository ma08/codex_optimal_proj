# -*- coding: utf-8 -*-

import sys

def main():
    s = raw_input()
    t = raw_input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()

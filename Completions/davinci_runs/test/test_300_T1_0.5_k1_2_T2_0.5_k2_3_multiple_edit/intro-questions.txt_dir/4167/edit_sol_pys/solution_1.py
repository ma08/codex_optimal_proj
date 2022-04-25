# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import sys

def main():
    s = sys.stdin.readline()
    t = sys.stdin.readline()

    for i in range(len(s)):
        print('Yes' if s[i] == t[i] else 'No')

if __name__ == '__main__':
    main()

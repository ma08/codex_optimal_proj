#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: omi
# @Date:   2014-08-24 21:51:57
# @Last Modified by:   omi
# @Last Modified time: 2014-08-24 21:51:57

import sys

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = [i[0] for i in s if i[0] in ['M', 'A', 'R', 'C', 'H']]
    s = list(set(s))
    print(len(s) * (len(s) - 1) * (len(s) - 2) // 6)

if __name__ == '__main__':
    main()

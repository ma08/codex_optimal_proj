
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 14:48:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys


def main():
    n = int(input())
    a = [0] * 1000000
    for i in range(n):
        a[int(input())] += 1
    print(sum(map(lambda x: x % 2, a)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-06-06 12:49:10
# @Last Modified by: Shuailong
# @Last Modified time: 2019-06-06 12:49:10

import sys

def main():
    k = int(sys.stdin.readline().strip())
    i = 1
    while True:
        if not (7 * (10 ** i) - 7) % k:
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()

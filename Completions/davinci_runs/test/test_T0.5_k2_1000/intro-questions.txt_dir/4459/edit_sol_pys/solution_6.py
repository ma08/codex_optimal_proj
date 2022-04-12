#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-12 22:10:58
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-12 22:15:32

import sys

def main():
    n = int(sys.stdin.readline())
    a = sorted(map(int, sys.stdin.readline().strip().split()), reverse=True)
    ans = 0
    for i in range(n):
        if a[i] < i + 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()

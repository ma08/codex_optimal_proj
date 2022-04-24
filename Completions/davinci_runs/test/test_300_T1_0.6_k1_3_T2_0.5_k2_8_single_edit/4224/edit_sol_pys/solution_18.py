#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-10 15:23:34
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


import os



def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        cnt = 0
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
                cnt += 1
        if cnt == 0:
            break
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()

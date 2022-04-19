#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(1, n):
        if s[i - 1] == s[i]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a = set(a)
    print(len(a))

if __name__ == '__main__':
    main()

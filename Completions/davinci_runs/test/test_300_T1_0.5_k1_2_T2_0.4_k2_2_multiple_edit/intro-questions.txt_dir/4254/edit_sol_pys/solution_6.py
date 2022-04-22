#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    sheep, wolf = map(int, sys.stdin.readline().split())  # 入力

    if sheep < wolf:
        print("unsafe")  # 出力
    else:
        print("safe")  # 出力

if __name__ == '__main__':
    main()

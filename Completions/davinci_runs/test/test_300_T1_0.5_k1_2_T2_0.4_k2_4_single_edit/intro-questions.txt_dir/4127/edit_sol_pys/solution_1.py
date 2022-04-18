# -*- coding: utf-8 -*-

import sys

def main():
    A, B = map(float, sys.stdin.readline().split())
    print(int(A * B))  # 小数点以下切り捨て

if __name__ == '__main__':
    main()

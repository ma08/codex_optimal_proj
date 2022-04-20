# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    x = list(map(int, input().split())) # ここでxに数字を格納
    x.sort()
    if n % 2 == 0: # 偶数個の数字がある場合
        print(x[n//2] - x[n//2 - 1])
    else: # 奇数個の数字がある場合
        print(0)

if __name__ == "__main__":
    main()

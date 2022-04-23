# -*- coding: utf-8 -*-

import sys

def main():
    N, M, C = map(int, sys.stdin.readline().split())
    B = list(map(int, sys.stdin.readline().split()))
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    count = 0  # 電気がつくアパートの個数
    for i in range(N):  # 縦
        total = 0  # i番目のアパートで電気がつくかどうかを判断するための変数
        for j in range(M):  # 横
            total += A[i][j] * B[j]
        if total + C > 0:  # 電気がつく
            count += 1
    print(count)  # 電気がつくアパートの個数

if __name__ == '__main__':
    main()

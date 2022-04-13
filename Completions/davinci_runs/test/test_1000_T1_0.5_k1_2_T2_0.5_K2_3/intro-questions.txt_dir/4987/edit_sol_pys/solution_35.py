# -*- coding: utf-8 -*-

import sys

def main():
    N, M = [int(i) for i in sys.stdin.readline().split()]  # N=スキー場の総数, M=クラスの総数
    S = [int(i) for i in sys.stdin.readline().split()]  # S=スキー場の距離
    S.sort()
    # print(N, M, S)
    if len(S) == 1:
        print(0)
        return
    if len(S) == 2:
        print(S[1]-S[0])
        return
    d = []
    for i in range(len(S)-1):
        d.append(S[i+1]-S[i])
    d.sort(reverse=True)
    # print(d)
    ans = 0
    for i in range(M-1):
        ans += d[i]
    print(ans)

if __name__ == '__main__':
    main()

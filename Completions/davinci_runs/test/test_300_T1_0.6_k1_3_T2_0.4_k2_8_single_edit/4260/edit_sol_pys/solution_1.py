#1時間で何秒かかるか計算して、その秒数を掛け算する(問題文に記載されている時間は分単位なので、それを秒単位に変換する必要がある)
import sys
input = sys.stdin.readline

T,X = map(int, input().split())

print(T / X)

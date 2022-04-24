
# 入力された数値から、1時間で何秒かかるか計算して、その秒数を掛け算する
import sys
input = sys.stdin.readline

T,X = map(int, input().split())

print(T / X)

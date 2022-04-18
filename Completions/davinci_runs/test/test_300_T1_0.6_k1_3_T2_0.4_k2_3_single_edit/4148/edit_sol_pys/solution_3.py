#!/usr/bin/env python3

import string

N = int(input())
S = input()

# 文字列の先頭からAを差し引いた数を求める
A = ord(string.ascii_uppercase[0])

# 全部の文字を1文字ずつ処理する
for ch in S:
    # 文字chが何文字目か調べる
    pos = ord(ch) - A
    # Nを足す
    pos = (pos + N) % 26
    # 1文字ずつ出力する
    print(chr(pos + A), end='')

print()


import string

N = int(input())  # 文字列の先頭からAを差し引いた数を求める
S = input()  # 全部の文字を1文字ずつ処理する

A = ord(string.ascii_uppercase[0])

for ch in S:
    pos = ord(ch) - A
    pos = (pos + N) % 26
    print(chr(pos + A), end='')

print()

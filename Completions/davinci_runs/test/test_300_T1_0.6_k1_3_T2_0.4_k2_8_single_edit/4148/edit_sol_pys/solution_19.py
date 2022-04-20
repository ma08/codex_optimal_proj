import string



N = int(input())
S = input()

A = ord(string.ascii_uppercase[0])

for ch in S:
    pos = ord(ch) - A
    pos = (pos + N) % 26
    # 1文字ずつ出力する
    print(chr(pos + A), end='')

print()

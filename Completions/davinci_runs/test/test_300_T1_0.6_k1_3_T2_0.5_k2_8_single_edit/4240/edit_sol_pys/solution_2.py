

from sys import stdin

s = stdin.readline().rstrip()  # strip()は文字列の前後の空白文字（スペース、タブ、改行）を削除してくれる
t = stdin.readline().rstrip()  # rstrip()は文字列の末尾の空白文字を削除してくれる

for _ in range(len(s)):
    s = s[-1] + s[:-1]  # s[-1]は最後の文字、s[:-1]は最後の文字を除いた文字列
    if s == t:
        print("Yes")
        exit()

print("No")

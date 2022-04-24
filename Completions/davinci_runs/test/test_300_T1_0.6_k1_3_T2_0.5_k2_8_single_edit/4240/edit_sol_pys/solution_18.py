
from sys import stdin

s = stdin.readline().rstrip()
t = stdin.readline().rstrip()

for _ in range(len(s)):
    s = s[-1] + s[:-1] # 末尾の文字を先頭に移動
    if s == t:
        print("Yes")
        exit()

print("No")

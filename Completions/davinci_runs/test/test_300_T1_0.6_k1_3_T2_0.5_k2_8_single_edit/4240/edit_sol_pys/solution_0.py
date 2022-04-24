

from sys import stdin

s = input()
t = input()

for _ in range(len(s)):
    s = s[-1] + s[:-1] #右に1つずつずらしていく
    if s == t:
        print("Yes")
        exit()

print("No")

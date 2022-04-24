
from sys import stdin

s = stdin.readline().rstrip()
T = stdin.readline().rstrip()

for _ in range(len(s)):
    s = s[-1] + s[:-1]
    if s == T:
        print("Yes")
        exit()

print("No")

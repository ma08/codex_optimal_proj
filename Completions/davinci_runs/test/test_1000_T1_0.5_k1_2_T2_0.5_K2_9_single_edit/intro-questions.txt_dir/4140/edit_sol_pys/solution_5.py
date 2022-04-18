
from sys import stdin

s = stdin.readline().strip()
count = 0
prev = s[0]
for i in range(1, len(s)):
    if prev != s[i]:
        prev = s[i]
    else:
        count += 1

print(count)

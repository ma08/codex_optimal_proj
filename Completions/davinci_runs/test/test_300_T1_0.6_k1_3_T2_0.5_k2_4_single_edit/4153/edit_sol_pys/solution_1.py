

from sys import stdin

s = stdin.readline()
s = s.strip()
count = {}
count[s[0]] = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count[s[i]] += 1
    else:
        count[s[i]] = 1

print min(count.values()) * 2

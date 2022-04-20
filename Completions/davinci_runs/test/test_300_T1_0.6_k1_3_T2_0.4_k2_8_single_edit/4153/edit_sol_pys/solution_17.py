

from sys import stdin

s = stdin.readline()

# count the number of adjacent 0s and 1s
count = {}
c = s[0]
count[c] = 1
for i in range(1, len(s)):
    if s[i] == c:
        count[c] += 1
    else:
        c = s[i]
        count[c] = 1

print min(count.values()) * 2

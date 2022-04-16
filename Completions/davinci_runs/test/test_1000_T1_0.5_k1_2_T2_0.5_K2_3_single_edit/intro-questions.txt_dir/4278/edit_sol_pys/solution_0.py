

import sys

n = int(input())
s = [input() for _ in range(n)]

anagrams = {}
for i in range(n):
    chars = list(s[i])
    chars.sort()
    key = "".join(chars)
    if key in anagrams:
        anagrams[key].append(i)
    else:
        anagrams[key] = [i]

count = 0
for key in anagrams:
    if len(anagrams[key]) >= 2:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2

print(count)

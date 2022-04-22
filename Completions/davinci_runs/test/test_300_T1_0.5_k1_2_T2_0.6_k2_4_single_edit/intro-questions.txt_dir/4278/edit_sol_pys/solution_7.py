

# my solution


import sys

# read input
n = int(sys.stdin.readline().rstrip())
s = []
for i in range(n):
    s.append(sys.stdin.readline().rstrip())

# create a dictionary of anagrams
anagrams = {}
for i in range(n):
    # sort characters
    chars = list(s[i])
    chars.sort()
    # create a key for the dictionary
    key = "".join(chars)
    if key in anagrams:
        anagrams[key].append(i)
    else:
        anagrams[key] = [i]

# count the number of pairs
count = 0
for key in anagrams:
    if len(anagrams[key]) >= 2:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2

# print the result
print(count)

# a better solution
import sys

n = int(sys.stdin.readline())

s = []
for _ in range(n):
    s.append(sys.stdin.readline().rstrip())

m = dict()
for i in range(n):
    m.setdefault("".join(sorted(s[i])), []).append(i)

ans = 0
for i in m.values():
    ans += len(i) * (len(i) - 1) // 2

print(ans)

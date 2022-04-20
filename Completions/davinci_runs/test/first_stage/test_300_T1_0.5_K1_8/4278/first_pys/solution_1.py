

from collections import Counter

# read input
N = int(input())
s = []
for i in range(N):
    s.append(input())

# sort the string
s_sorted = [''.join(sorted(x)) for x in s]

# count the number of pairs of anagrams
c = Counter(s_sorted)
ans = 0
for key in c.keys():
    ans += c[key] * (c[key]-1) // 2

print(ans)
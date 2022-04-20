

#https://codeforces.com/gym/101958/problem/C

n, k = map(int, input().split())
s = list(map(int, input().split()))

from collections import Counter

c = Counter(s)

for i in range(k):
    print(c.most_common()[0][0])
    c[c.most_common()[0][0]] -= 1
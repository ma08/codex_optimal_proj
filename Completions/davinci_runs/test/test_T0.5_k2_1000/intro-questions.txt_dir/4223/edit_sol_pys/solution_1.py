
# https://atcoder.jp/contests/abc137/tasks/abc137_a
from collections import Counter

n = int(input())
s = input()

c = Counter(s)

ans = n - sum(c.values())

print(ans)


import collections
# from collections import Counter
# n = int(input())
# c = Counter([input().split()[1] for _ in range(n)])
# print(c['soft']*c['hard'])

n = int(input())
c = collections.Counter()
for _ in range(n):
    name, kind = input().split()
    c[kind] += 1
print(c['soft']*c['hard'])

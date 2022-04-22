
# from collections import Counter
# n = int(input())
# a = list(map(int, input().split()))
#
# c = Counter(a)
# print(n-sum(map(lambda x: x % 2, c.values())))
# Solution

n = int(input())
a = list(map(int, input().split()))

s = set()
for i in range(n):
    if a[i] not in s:
        s.add(a[i])
    else:
        s.remove(a[i])

print(n - len(s))

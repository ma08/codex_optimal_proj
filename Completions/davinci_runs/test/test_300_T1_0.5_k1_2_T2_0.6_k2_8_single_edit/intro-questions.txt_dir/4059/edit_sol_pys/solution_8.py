from collections import Counter


N, M = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
s = sum(c.values())

print(count)

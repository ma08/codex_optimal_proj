import collections

n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)

if len(c) == n:
    print("YES")
else:
    print("NO")

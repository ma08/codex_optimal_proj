

#------------------------------------------------------------------------------#

n, V = map(int, input().split())
volumes = []
for _ in range(n):
    l, w, h = map(int, input().split())
    volumes.append(l * w * h)

#------------------------------------------------------------------------------#

from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)
for i in range(1, n+1):
    d[input()].append(i)

for _ in range(m):
    word = input()
    if word in d:
        print(*d[word])
    else:
        print(-1)

#------------------------------------------------------------------------------#

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) > sum(b):
    print('YES')
else:
    print('NO')

#------------------------------------------------------------------------------#

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

print(a[-k])

print(max(volumes) - V)

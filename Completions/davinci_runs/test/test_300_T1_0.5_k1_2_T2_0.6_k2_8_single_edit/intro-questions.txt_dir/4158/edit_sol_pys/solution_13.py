

n = int(input())
l = list(map(int, input().split()))

m = 0
d = {}

for x in l:
    if x in d:
        continue
    d[x] = 1
    for j in range(32):
        if x + 2**j in d:
            d[x + 2**j] = d[x] + 1
        if x - 2**j in d:
            d[x - 2**j] = d[x] + 1
        m = max(m, d[x])

print(m)

for i in l:
    if d[i] == m:
        print(i, end=' ')

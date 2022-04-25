
n = int(input())
l = list(map(int, input().split()))

m = 1
d = {}

d[l[0]] = 1

for i in l:
    if i in d:
        d[i] = 1
    for j in range(32):
        if i + 2**j in d:
            d[i + 2**j] = d[i] + 1
        if i - 2**j in d:
            d[i - 2**j] = d[i] + 1
        m = max(m, d[i + 2**j], d[i - 2**j])

print(m)

for i in l:
    if d[i] == m:
        print(i, end=' ')

n = int(input())
l = input().split()


m = -1
d = {}

for i in range(len(l)):
    l[i] = int(l[i])

for i in l:
    if i in d:
        continue
    d[i] = 1
    for j in range(32):
        if i + 2**j in d:
            d[i + 2**j] = d[i] + 1
        if i - 2**j in d:
            d[i - 2**j] = d[i] + 1
        m = max(m, d[i])

print(m)

for i in l:
    if d[i] == m:
        print(i, end=' ')

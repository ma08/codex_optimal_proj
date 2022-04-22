
n = int(input())
l = list(map(int, input().split()))

m = 0
d = {}

for i in l:
    if i in d:
        continue
    d[i] = [i]
    for j in range(32):
        if i + 2**j in d:
            d[i + 2**j] = d[i] + [i + 2**j]
        if i - 2**j in d:
            d[i - 2**j] = d[i] + [i - 2**j]
        m = max(m, len(d[i]))

print(m)

for i in l:
    if len(d[i]) == m:
        print(*d[i])

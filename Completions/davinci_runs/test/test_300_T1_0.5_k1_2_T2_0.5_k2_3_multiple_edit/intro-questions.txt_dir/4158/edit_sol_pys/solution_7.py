
n = int(input())
l = list(map(int, input().split()))

m = 0
d = {}
s = set()

for i in l:
    d[i] = 0
    for j in range(32):
        if i + 2**j in d or i + 2**j in s:
            d[i] += 1
        if i - 2**j in d or i - 2**j in s:
            d[i] += 1
        m = max(m, d[i] + 1)

print(m - 1)

for i in l:
    if d[i] == m - 1:
        print(i, end=' ')

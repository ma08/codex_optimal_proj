n = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    if i in d:
        continue
    d[i] = 1
    for j in range(32):
        if i + 2**j in d:
            d[i + 2**j] = d[i] + 1
        if i - 2**j in d:
            d[i - 2**j] = d[i] + 1
print(max(d.values()))

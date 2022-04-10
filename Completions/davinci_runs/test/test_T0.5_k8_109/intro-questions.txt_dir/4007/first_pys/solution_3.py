

n = int(input())
f = list(map(int, input().split()))

# print(n, f)

gift_to = {}
gift_from = {}
for i in range(n):
    if f[i] == 0:
        continue
    gift_to[f[i]] = i
    gift_from[i] = f[i]

# print(gift_to, gift_from)

for i in range(n):
    if f[i] != 0:
        continue
    for j in range(1, n + 1):
        if j in gift_to:
            continue
        f[i] = j
        gift_to[j] = i
        break

# print(f, gift_to)

for i in range(n):
    if f[i] == 0:
        continue
    for j in range(1, n + 1):
        if j in gift_from:
            continue
        gift_from[i] = j
        break

# print(f, gift_from)

for i in range(n):
    f[i] = gift_from[i]

print(*f)
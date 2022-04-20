
n, w = map(int, input().split())
a = list(map(int, input().split()))

l = [0] * (n + 1)
for i in range(1, n + 1):
    l[i] = l[i - 1] + a[i - 1]

r = [0] * (w + l[n] + 1)
r[w + l[0]] = 1
for i in range(1, n + 1):
    for j in range(w + l[i], l[i - 1], -1):
        if r[j] > 0:
            r[j + a[i - 1]] += r[j]

print(r[w + l[n]])

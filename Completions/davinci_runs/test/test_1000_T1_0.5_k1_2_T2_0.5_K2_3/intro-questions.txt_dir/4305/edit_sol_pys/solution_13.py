
n, x = map(int, input().split())
l = list(map(int, input().split()))
d = 0
for i in range(n):
    if i == 0:
        d += l[i]
    else:
        d += l[i] + x
print(d)

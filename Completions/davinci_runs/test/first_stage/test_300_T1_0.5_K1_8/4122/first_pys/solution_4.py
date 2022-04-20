

H, n = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

if H <= 0:
    print(1)
    exit()

h = H
for i in range(n):
    h += d[i]
    if h <= 0:
        print(i + 1)
        exit()

print(-1)
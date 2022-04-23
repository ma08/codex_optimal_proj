
H, n = map(int, input().split())
d = map(int, input().split())

for i in range(n):
    H += d[i]
    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)

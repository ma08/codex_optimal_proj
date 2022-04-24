

H, N = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

for i in range(N):
    H += d[i]
    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)

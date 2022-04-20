

# Solution 1

H, n = map(int, input().split())
d = list(map(int, input().split()))

for i in range(n):
    H += d[i]
    if H <= 0:
        print(i + 1)
        break
else:

# Solution 2

H, n = map(int, input().split())
d = list(map(int, input().split()))

for i in range(n):
    H += d[i]
    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)
    print(-1)


# Solution

H, n = map(int, input().split())
d = list(map(int, input().split()))

hp = H
minute = 0

for i in range(n):
    H += d[i]
    minute += 1
    if H <= 0:
        print(minute)
        break
else:
    print(-1)

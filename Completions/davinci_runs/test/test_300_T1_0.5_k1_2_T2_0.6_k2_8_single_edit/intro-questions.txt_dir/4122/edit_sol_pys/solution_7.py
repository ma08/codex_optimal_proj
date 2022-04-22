

# Solution 1

H, n = map(int, input().split())
d = list(map(int, input().split()))

hp = H
minute = 0

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        print(minute)
        break
else:

# Solution 2

h, n = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    h -= a[i]
    if h <= 0:
        print(i + 1)
        break
else:
    print(-1)
    print(-1)

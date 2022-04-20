

# Solution

h, n = map(int, input().split())
a = list(map(int, input().split()))

hp = h
minute = 0

for i in range(n):
    hp -= a[i]
    minute += 1
    if hp <= 0:
        print(minute)
        break
else:
    print(-1)

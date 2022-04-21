
# Solution

H, n = map(int, input().split())  # H is the initial HP of the monster, n is the number of attacks
d = list(map(int, input().split()))  # d is the list of damage

hp = H
minute = 0

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        print(minute)
        break
else:
    print(-1)

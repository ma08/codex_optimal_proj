
# Solution

H, n = map(int, input().split())  # H: HP, n: number of spells
d = list(map(int, input().split()))  # d: list of spells

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

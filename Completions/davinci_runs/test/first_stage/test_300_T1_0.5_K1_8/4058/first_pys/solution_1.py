

n, r = map(int, raw_input().split())

a = map(int, raw_input().split())

heaters = []

for i in range(n):
    if a[i] == 1:
        heaters.append(i)

#print heaters

if len(heaters) == 0:
    print -1
    exit()

heaters.sort()

#print heaters

heaters.append(n)

ans = 1

last = heaters[0] + r - 1

#print last

for i in range(1, len(heaters)):
    if heaters[i] - r + 1 <= last:
        last = max(last, heaters[i] + r - 1)
    else:
        ans += 1
        last = heaters[i] + r - 1

print ans
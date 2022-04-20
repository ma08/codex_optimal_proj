

n, x = map(int, input().split())
l = map(int, input().split())

bounce = 0
d = 0

for i in range(n):
    if d <= x:
        bounce += 1
    d += l[i]

if d <= x:
    bounce += 1

print(bounce)
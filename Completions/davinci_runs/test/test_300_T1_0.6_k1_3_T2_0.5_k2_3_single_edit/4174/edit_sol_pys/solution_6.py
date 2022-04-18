
n, x = map(int, input().split())
l = list(map(int, input().split()))

count = 0
d = 0

for i in range(n-1):
    d += l[i]
    if d <= x:
        count += 1

print(count)

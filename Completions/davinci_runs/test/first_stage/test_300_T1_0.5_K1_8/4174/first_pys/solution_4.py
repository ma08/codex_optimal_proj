

n, x = map(int, input().split())
l = list(map(int, input().split()))

d = 0
count = 0
for i in l:
    d += i
    if d <= x:
        count += 1

print(count + 1)
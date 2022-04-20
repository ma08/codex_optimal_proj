
n, x = map(int, input().split())
l = list(map(int, input().split()))

# 初期値
count = 1
d = 0

for i in range(n-1):
    d += l[i]
    if d <= x:
        count += 1

print(count)

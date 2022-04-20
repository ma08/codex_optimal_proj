

n = int(input())
d = list(map(int, input().split()))

d.sort()

if n % 2 == 0:
    mid_index = n // 2
else:
    mid_index = n // 2

mid = d[mid_index]

count = 0
for i in range(mid_index + 1, n):
    if d[i] == mid:
        count += 1

print(count + 1)

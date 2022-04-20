

n = int(input())
a = list(map(int, input().split()))

cur = 1
max = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        cur += 1
    else:
        if cur > max:
            max = cur
        cur = 1
if cur > max:
    max = cur

print(max)


n = int(input())
a = list(map(int, input().split()))

a.sort()

max = a[0]
for i in range(1, n):
    if max < a[i]:
        max = a[i]
    a[i] = max + a[i]

print(a[-1] + 1)

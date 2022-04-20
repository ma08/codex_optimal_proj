

h, n = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

for i in range(1, n + 1):
    h -= a[i - 1]
    if h <= 0:
        print(i + 1)
        break
print(-1)

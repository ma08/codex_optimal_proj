

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

c = 0
for i in range(n):
    if a[i] <= x:
        c += 1
    else:
        break
print(c)

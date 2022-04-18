

n, m = map(int, input().split()) # n, m = 5, 3
a = list(map(int, input().split())) # a = [3, 1, 4]

a.sort()

if a[-1] > n:
    print(-1)
    exit()

s = 0
for i in range(m):
    s += a[i]

print(n - s)

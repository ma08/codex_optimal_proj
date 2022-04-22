

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

if a[0] > n:
    print(-1)
    exit()

s = 0
for i in range(m):
    s += a[i]


print(n - s)

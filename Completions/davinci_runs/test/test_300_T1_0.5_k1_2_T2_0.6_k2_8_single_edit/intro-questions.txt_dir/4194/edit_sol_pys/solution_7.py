
n, m = map(int, input().split())
a = list(map(int, input().split()))[:m]

a.sort()

if a[-1] > n:
    print(-1)
    exit()

s = 0
for i in a:
    s += i

print(n - s)

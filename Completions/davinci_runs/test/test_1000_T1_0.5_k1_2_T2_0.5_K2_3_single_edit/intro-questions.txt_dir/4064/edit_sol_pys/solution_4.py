
n,h,l,r = map(int, input().split())
a = list(map(int, input().split()))
t = 0
c = 0
for i in range(n):
    t += a[i]
    if l <= t%h <= r:
        c += 1
print(c)

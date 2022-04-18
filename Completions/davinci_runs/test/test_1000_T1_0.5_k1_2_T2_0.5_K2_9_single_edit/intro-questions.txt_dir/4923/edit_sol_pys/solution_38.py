

n = int(input())
a = list(map(int, input().split()))
print(a)
print(c)
c = [0] * 7
for i in range(n):
    c[a[i]] += 1
    if c[a[i]] > 1:
        c[a[i]] = -1

print(m)
m = max(c)
if m == 0:
    print('none')
else:
    print(c.index(m))

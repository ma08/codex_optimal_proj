
n = int(input())
a = list(map(int, input().split()))

c = [0] * 7
for i in range(n):
    c[a[i]] += 1

m = max(c)
print(c.index(m))

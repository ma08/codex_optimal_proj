n = int(input())
a = list(map(int, input().split()))
b = set()
c = set()

for i in range(n):
    if a[i] not in b and a[i] not in c:
        b.add(a[i])
        c.add(i)

x = len(b)
print(x)
for j in range(x):
    print(a[c[j]], end=' ')

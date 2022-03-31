

n = int(input())
a = list(map(int, input().split()))
b = []
c = []

for i in range(n):
    if a[i] not in b:
        b.append(a[i])
        c.append(i)

x = len(b)
print(x)
for j in range(x):
    print(a[c[j]], end=' ')
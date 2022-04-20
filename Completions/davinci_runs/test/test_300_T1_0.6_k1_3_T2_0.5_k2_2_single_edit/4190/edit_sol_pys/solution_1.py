

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
for i in range(n):
    c.append((a[i]+b[i])%n)

c2 = sorted(c)

for i in range(n):
    b[c.index(c2[i])] = i+1

print(" ".join(map(str, b)))

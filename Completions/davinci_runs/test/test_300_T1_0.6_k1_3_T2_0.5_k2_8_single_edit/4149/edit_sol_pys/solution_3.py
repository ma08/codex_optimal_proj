
n = int(input())
a = [int(x) for x in input().split()]

b = []

for i in range(n):
    if a[i] in a[n:]:
        b.append(a[i])

print(*b)

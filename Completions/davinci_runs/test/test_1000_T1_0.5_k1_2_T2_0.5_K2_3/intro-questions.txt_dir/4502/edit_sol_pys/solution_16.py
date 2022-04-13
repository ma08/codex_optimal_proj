

n = int(input())
a = [int(s) for s in input().split()]

b = []
for i in range(n):
    b.append(a[i])

b.reverse()

print(*b)

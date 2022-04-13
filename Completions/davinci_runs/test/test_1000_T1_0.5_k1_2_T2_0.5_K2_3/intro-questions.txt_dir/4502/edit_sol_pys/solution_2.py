
n = int(input())
a = [int(s) for s in input().split()]

for i in range(n):
    a.insert(i, a[i])
    a.reverse()

print(*a)

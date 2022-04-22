

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

s = 0

for i in range(n):
    c = min(a[i], b[i])
    s += c
    a[i] -= c
    b[i] -= c

    c = min(a[i+1], b[i])
    s += c
    a[i+1] -= c
    b[i] -= c

print(n - s)


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

d = 0
for i in range(n):
    d += b[a[i]-1]
    if i != n-1:
        if a[i] == a[i+1]-1:
            d += c[a[i]-1]

print(d)
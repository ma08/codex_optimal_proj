

n = int(input())
a = [int(x) for x in input().split()]

d = a[0]
for i in range(1, n):
    d = gcd(d, a[i])
print(d)

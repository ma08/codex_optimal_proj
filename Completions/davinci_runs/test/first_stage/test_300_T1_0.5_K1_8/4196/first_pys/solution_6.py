

n = int(input())
a = list(map(int, input().split()))

gcd_a = a[0]
for i in range(1, n):
    gcd_a = gcd(gcd_a, a[i])

print(gcd_a)
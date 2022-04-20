

# n = int(input())
# a = list(map(int, input().split()))
n = 3
a = [7, 6, 8]

gcd_a = a[0]
for i in range(1, n):
    gcd_a = math.gcd(gcd_a, a[i])

max_gcd = 0
for i in range(n):
    max_gcd = max(max_gcd, math.gcd(gcd_a, a[i]))

print(max_gcd)
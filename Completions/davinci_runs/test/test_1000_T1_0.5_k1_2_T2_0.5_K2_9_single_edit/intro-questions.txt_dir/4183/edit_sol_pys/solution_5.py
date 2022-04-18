import fractions

n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = fractions.gcd(gcd, t[i])

print(gcd)

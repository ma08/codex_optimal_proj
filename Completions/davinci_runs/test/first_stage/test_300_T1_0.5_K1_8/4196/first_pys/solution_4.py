

n = int(input())
a = list(map(int, input().split()))

gcd = 0
for i in range(n):
    if gcd == 1:
        break
    for j in range(i+1, n):
        if gcd == 1:
            break
        gcd = max(gcd, a[i]*a[j]//math.gcd(a[i], a[j]))

print(gcd)
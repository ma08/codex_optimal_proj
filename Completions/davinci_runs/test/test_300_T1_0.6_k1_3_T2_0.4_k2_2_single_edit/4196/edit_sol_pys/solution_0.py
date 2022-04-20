

n = int(input())
a = list(map(int, input().split()))

a.sort()
if a[0] == a[n-1]:
    print(a[0])
else:
    print(a[0]*a[n-1]//math.gcd(a[0], a[n-1])

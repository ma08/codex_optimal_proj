

n, k = map(int, input().split())

if n % 10**k >= 5*10**(k-1):
    print(n + (10**k - n % 10**k))
else:
    print(n - n % 10**k)

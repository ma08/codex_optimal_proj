

c, k = map(int, input().split())

if c % 10**k >= 5*10**(k-1):
    print(c + (10**k - c % 10**k))
else:
    print(c - c % 10**k)
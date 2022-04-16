
c, k = [int(x) for x in input().split()]
c -= c % (10**k)
print(c)

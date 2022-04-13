

k, n = [int(x) for x in input().split()]
k -= k % (10**n)
print(k)



# put your python code here
n, k = [int(x) for x in input().split()]
n -= n % (10**k)
print(n)



# read the input
n, k = map(int, input().split())
p = list(map(int, input().split()))

# sort the prices
p.sort()

# get the first k prices
minimum = sum(p[:k])

# print the result
print(minimum)
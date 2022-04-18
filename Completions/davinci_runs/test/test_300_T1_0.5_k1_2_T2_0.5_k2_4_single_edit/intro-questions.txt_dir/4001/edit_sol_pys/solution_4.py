

# read N and K
N, K = map(int, input().split())
# read list of numbers
L = list(map(int, input().split()))[:N]

# sort list in ascending order
L.sort()

# print Kth smallest number
print(L[K-1])


# input
N, K = map(int, input().split())
p = list(map(int, input().split()))[:N]

# sort
p.sort()

# output
print(sum(p[:K]))

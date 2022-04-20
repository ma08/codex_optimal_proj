

# input
N, K = map(int, input().split())
p = list(map(int, input().split()))

# sort
p.sort()

# output
print(sum(p[:K]))
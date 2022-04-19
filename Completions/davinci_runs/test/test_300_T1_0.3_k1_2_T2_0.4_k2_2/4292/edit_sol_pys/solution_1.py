
# input
N, K = map(int, input().split())
p = list(map(int, input().split()))

# output
print(sum(sorted(p)[:K]))

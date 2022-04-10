

n, m = map(int, input().split())
a = list(map(int, input().split()))

# Get the number of elements <= m
l = [1 if x <= m else 0 for x in a]

# Get the prefix sums
p = [0]
for i in l:
    p.append(p[-1] + i)

# Get the number of pairs of indices (l,r) where p[l] = p[r]
# That is, the number of pairs of indices (l,r) such that
# p[r] - p[l] = 0
# p[r] - p[l] = 1
# p[r] - p[l] = 2
# ...
# p[r] - p[l] = p[r]
# The number of pairs of indices (l,r) such that p[r] - p[l] = i
# is equal to the number of indices l such that p[l] = i
# so we can simply count the number of indices l such that p[l] = i

# Get the number of indices l such that p[l] = i
counts = [0] * (n + 1)
for i in p:
    counts[i] += 1

# Get the number of pairs of indices (l,r) where p[l] = p[r]
ans = 0
for i in counts:
    ans += i * (i - 1) // 2

print(ans)
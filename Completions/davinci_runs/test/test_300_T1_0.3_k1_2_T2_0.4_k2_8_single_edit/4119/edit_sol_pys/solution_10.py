

# input N and M

# input x
n, m = map(int, input().split())
x = list(map(int, input().split()))

# sort x
x.sort()

# get the median of x
median = x[m // 2]

# calculate the distance between x and median
ans = 0
for i in range(m):
    ans += abs(x[i] - median)

print(ans)

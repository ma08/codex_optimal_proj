

# input the number of elements and the number of queries
n, m = map(int, input().split())

# input the elements
x = list(map(int, input().split()))
x = list(map(int, input().split()))

# sort
x.sort()

# get the median
median = x[m // 2]

# calculate the distance
ans = 0
for i in range(m):
    ans += abs(x[i] - median)

print(ans)

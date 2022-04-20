
# input
n, m = map(int, input().split())
x = list(map(int, input().split()))  # list of integers

# sort
x.sort()

# get the median (odd number of elements)
if m % 2 == 1:
    median = x[m // 2]
else:
    median = (x[m // 2] + x[m // 2 - 1]) / 2

# calculate the distance
ans = 0
for i in range(m):
    ans += abs(x[i] - median)

print(ans)

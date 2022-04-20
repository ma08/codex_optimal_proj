
# Solution

n, w = [int(x) for x in input().split()]  # n: number of items, w: weight
a = [int(x) for x in input().split()]  # a: weight of each item

x = [0] * (n + 1)  # x: prefix sum of a

for i in range(1, n + 1):
    x[i] = x[i - 1] + a[i - 1]  # calculate prefix sum of a

x.sort()  # sort x

ans = 0  # answer

for i in range(1, n + 1):
    if x[i] - x[i - 1] > 0:  # if x[i] - x[i - 1] > 0, add it to answer
        ans += x[i] - x[i - 1]  # add x[i] - x[i - 1] to answer

print(min(ans, w + 1))

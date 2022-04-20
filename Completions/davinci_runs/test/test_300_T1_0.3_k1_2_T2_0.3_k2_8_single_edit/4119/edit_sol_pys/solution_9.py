# coding:utf-8

# input
n, m = map(int, input().split())
x = list(map(int, input().split()))

# sort
x.sort()

# get the median (中央値)
median = x[m // 2]  # 割り算の余りを切り捨てる

# calculate the distance
ans = 0
for i in range(m):
    ans += abs(x[i] - median)

print(ans)

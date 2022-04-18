import math


N = int(input())  # データ数
data = [int(input()) for _ in range(N)]  # データ

# 平均
mean = sum(data) / N
# 分散
variance = sum([(x - mean) ** 2 for x in data]) / N
# 標準偏差
stdev = math.sqrt(variance)

print(variance)
print(stdev)

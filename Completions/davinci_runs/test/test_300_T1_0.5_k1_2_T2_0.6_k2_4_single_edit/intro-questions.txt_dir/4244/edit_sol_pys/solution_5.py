

n = int(input())
x = list(map(int, input().split()))

x_min = min(x)  # 最小値
x_max = max(x)  # 最大値

x_sum = sum(x)  # 合計

x_min_sum = 0  # 最小値からの差の二乗の合計
for i in range(n):
    x_min_sum += (x[i] - x_min) ** 2

x_max_sum = 0  # 最大値からの差の二乗の合計
for i in range(n):
    x_max_sum += (x[i] - x_max) ** 2

x_sum_sum = 0  # 平均からの差の二乗の合計
for i in range(n):
    x_sum_sum += (x[i] - x_sum / n) ** 2

print(min(x_min_sum, x_max_sum, x_sum_sum))

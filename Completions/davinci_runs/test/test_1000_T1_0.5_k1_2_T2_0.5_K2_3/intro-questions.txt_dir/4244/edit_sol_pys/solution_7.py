
import math

n = int(input())
x = list(map(int, input().split()))

x_min = int(min(x))
x_max = int(max(x))

x_sum = int(sum(x) / n)

x_min_sum = 0
for i in range(n):
    x_min_sum += (x[i] - x_min) ** 2

x_max_sum = 0
for i in range(n):
    x_max_sum += (x[i] - x_max) ** 2

x_sum_sum = 0
for i in range(n):
    x_sum_sum += (x[i] - x_sum) ** 2

print(min(x_min_sum, x_max_sum, x_sum_sum))

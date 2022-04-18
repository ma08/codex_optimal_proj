
import sys

sys.setrecursionlimit(1000000)


def f(n, x, x_min, x_max, x_sum, x_min_sum, x_max_sum, x_sum_sum, i):
    if i == n:
        return min(x_min_sum, x_max_sum, x_sum_sum)
    else:
        x_min_sum += (x[i] - x_min) ** 2
        x_max_sum += (x[i] - x_max) ** 2
        x_sum_sum += (x[i] - x_sum / n) ** 2
        return f(n, x, x_min, x_max, x_sum, x_min_sum, x_max_sum, x_sum_sum, i + 1)


n = int(input())
x = list(map(int, input().split()))

x_min = min(x)
x_max = max(x)

x_sum = sum(x)

x_min_sum = 0
for i in range(n):
    x_min_sum += (x[i] - x_min) ** 2

x_max_sum = 0
for i in range(n):
    x_max_sum += (x[i] - x_max) ** 2

x_sum_sum = 0
for i in range(n):
    x_sum_sum += (x[i] - x_sum / n) ** 2

print(min(x_min_sum, x_max_sum, x_sum_sum))

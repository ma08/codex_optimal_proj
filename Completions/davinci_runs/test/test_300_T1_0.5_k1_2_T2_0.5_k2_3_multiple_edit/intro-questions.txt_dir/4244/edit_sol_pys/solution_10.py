
n = int(input())
x = list(map(int, input().split()))

x_min = x[0]
x_max = x[0]
for i in range(n):
    if x_min > x[i]:
        x_min = x[i]
    if x_max < x[i]:
        x_max = x[i]

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

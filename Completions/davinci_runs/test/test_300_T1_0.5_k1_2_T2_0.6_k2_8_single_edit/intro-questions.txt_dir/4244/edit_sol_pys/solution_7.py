

n = int(input())
x_list = list(map(int, input().split()))

x_min = min(x_list)
x_max = max(x_list)

x_sum = sum(x_list)

x_min_sum = 0
for i in range(n):
    x_min_sum += (x_list[i] - x_min) ** 2

x_max_sum = 0
for i in range(n):
    x_max_sum += (x_list[i] - x_max) ** 2

x_sum_sum = 0
for i in range(n):
    x_sum_sum += (x_list[i] - x_sum / n) ** 2

print(min(x_min_sum, x_max_sum, x_sum_sum))

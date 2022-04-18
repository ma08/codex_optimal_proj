

n = int(input())
x = list(map(int, input().split()))
print(x)
x_min = min(x)
x_max = max(x)
print(x_min)
print(x_max)
x_sum = sum(x)
print(x_sum)
x_min_sum = 0
for i in range(n):
    x_min_sum += (x[i] - x_min) ** 2
print(x_min_sum)
x_max_sum = 0
for i in range(n):
    x_max_sum += (x[i] - x_max) ** 2
print(x_max_sum)
x_sum_sum = 0
for i in range(n):
    x_sum_sum += (x[i] - x_sum / n) ** 2
print(x_sum_sum)
print(min(x_min_sum, x_max_sum, x_sum_sum))

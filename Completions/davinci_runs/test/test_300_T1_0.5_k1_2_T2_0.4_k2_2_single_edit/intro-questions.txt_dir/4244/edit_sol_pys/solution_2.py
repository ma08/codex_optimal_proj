

n = int(input())  # number of elements
x = list(map(int, input().split()))  # numbers

x_min = min(x)  # minimum value
x_max = max(x)  # maximum value

x_sum = sum(x)  # sum of all elements

x_min_sum = 0  # sum of squares of differences between each element and x_min
for i in range(n):
    x_min_sum += (x[i] - x_min) ** 2

x_max_sum = 0  # sum of squares of differences between each element and x_max
for i in range(n):
    x_max_sum += (x[i] - x_max) ** 2

x_sum_sum = 0  # sum of squares of differences between each element and x_sum / n
for i in range(n):
    x_sum_sum += (x[i] - x_sum / n) ** 2

print(min(x_min_sum, x_max_sum, x_sum_sum))

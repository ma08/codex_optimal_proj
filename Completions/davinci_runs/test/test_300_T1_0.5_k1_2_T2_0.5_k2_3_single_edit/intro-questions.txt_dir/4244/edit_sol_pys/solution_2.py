

n = int(input())

if n == 1:
    print(0)
    exit()
x = list(map(int, input().split()))

x_min = min(x)
x_max = max(x)

x_sum = sum(x)

x_min_sum = sum([(x[i] - x_min) ** 2 for i in range(n)])

x_max_sum = sum([(x[i] - x_max) ** 2 for i in range(n)])

x_sum_sum = 0
for i in range(n):
    x_sum_sum += (x[i] - x_sum / n) ** 2

print(min(x_min_sum, x_max_sum, x_sum_sum))

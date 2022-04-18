

n = int(input())
x = list(map(int, input().split()))

x_min = min(x)
x_max = max(x)

x_sum = sum(x) / n


def get_sum(x_i):
    x_sum = 0
    for i in range(n):
        x_sum += (x[i] - x_i) ** 2

x_min_sum = get_sum(x_min)
x_max_sum = get_sum(x_max)
x_sum_sum = get_sum(x_sum)

print(min(x_min_sum, x_max_sum, x_sum_sum))

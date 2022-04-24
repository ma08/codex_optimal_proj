

n = int(input())
x = list(map(int, input().split()))

x_min_sum = sum([(i - min(x)) ** 2 for i in x])
x_max_sum = sum([(i - max(x)) ** 2 for i in x])
x_sum_sum = sum([(i - sum(x) / n) ** 2 for i in x])

print(int(min(x_min_sum, x_max_sum, x_sum_sum)))

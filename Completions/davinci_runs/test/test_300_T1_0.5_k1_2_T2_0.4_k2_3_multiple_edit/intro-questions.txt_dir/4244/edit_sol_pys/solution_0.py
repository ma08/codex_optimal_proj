
n = int(input())
x = list(map(int, input().split()))

def variance(x_min):
    x_min_sum = 0
    for i in range(n):
        x_min_sum += (x[i] - x_min) ** 2
    return x_min_sum

print(min(x_min_sum, x_max_sum, x_sum_sum))

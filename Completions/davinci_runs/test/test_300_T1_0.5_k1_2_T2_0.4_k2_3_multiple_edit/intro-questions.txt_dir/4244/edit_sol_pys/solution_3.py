

n = int(input())  # 整数の入力
a = list(map(int, input().split()))  # 整数リストの入力

a_sum = sum(a)
a_min = min(a)
a_max = max(a)

a_min_sum = sum((a[i] - a_min) ** 2 for i in range(n))
a_max_sum = sum((a[i] - a_max) ** 2 for i in range(n))
a_sum_sum = sum((a[i] - a_sum / n) ** 2 for i in range(n))

print(min(a_min_sum, a_max_sum, a_sum_sum))  # 出力

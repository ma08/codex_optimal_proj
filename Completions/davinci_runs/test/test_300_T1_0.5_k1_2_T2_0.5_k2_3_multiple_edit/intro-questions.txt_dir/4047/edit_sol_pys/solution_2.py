

n = int(input())
x = list(map(int, input().split()))  # 複数数値入力
# x = [1, 2, 3]
# n = 3

x.sort()

min_cost = float('inf')
for i in range(n):
    cost = 0
    for j in range(n):
        cost += abs(x[j] - x[i])
    min_cost = min(min_cost, cost)

print(min_cost)

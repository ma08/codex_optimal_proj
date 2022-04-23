
n = int(input())
x = list(map(int, input().split()))

x.sort()

min_cost = float('inf')  # 正の最大値
for i in range(n):
    cost = 0
    for j in range(n):
        cost += abs(x[j] - x[i])
    min_cost = min(min_cost, cost)

print(min_cost)


n, m, x = map(int, input().split())
a_list = list(map(int, input().split()))

cost_1 = 0
cost_2 = 0

for i in range(x):
    if i + 1 in a_list:
        cost_1 += 1

for i in range(x, n):
    if i + 1 in a_list:
        cost_2 += 1

print(min(cost_1, cost_2))

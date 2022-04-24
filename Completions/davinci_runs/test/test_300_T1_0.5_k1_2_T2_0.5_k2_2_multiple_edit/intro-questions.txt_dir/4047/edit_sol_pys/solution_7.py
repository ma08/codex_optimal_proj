
n = int(input())
a = list(map(int, input().split()))

# a = [1, 2, 3]
# n = 3

a.sort()

min_cost = float('inf')
for i in range(n):
    cost = 0
    for j in range(n):
        cost += abs(a[j] - a[i])
    min_cost = min(min_cost, cost)

print(min_cost)

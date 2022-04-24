

N = int(input())
x = list(map(int, input().split()))

x.sort()


min_cost = float('inf')
for i in range(N):
    cost = 0  # cost is 0 at the beginning
    for j in range(N):
        cost += abs(x[j] - x[i])
    min_cost = min(min_cost, cost)


print(min_cost)



n = int(input())
x = list(map(int, input().split()))

def cost(a, x):
    return sum(abs(a - xi) for xi in x)

x.sort()

min_cost = float('inf')
for i in range(n):
    min_cost = min(min_cost, cost(x[i], x))

print(min_cost)



def min_cost(n, a, b):
    return min(a*(n//2) + b*(n%2), b*(n//2) + a*(n%2))

q = int(input())
for _ in range(q):
    n, a, b = map(int, input().split())
    print(min_cost(n, a, b))
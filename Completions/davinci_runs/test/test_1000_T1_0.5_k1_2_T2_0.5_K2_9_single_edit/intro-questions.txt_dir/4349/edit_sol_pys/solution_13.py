

n, m = map(int, input().split())
k = list(map(int, input().split()))

sales = {}

for _ in range(m):
    d, t = map(int, input().split())
    sales[d] = t


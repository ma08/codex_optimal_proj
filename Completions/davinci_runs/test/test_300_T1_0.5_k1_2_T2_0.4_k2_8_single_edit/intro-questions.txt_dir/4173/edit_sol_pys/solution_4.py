

q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]
    
    min_cost = n*a
    if a > b:
        min_cost = min(min_cost, n*b)
    
    print(min_cost)

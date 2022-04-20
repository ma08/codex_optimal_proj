

q = int(input())

for i in range(q):
    n, k, m = [int(x) for x in input().split()]
    
    min_bottles = n // 2
    min_cost = min_bottles * m + (n % 2) * k
    if k > m:
        min_cost = min(min_cost, (n // 2) * k + (n % 2) * m)
    
    print(min_cost)

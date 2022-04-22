

q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]
    
    min_bottles = n // 2 * b
    min_cost = min_bottles + (n % 2) * a
    if a > b:
        min_cost = min(min_cost, (n // 2) * a + (n % 2) * a)
    
    print(min_cost)


q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]
    
    min_bottles = n//2  # minimum number of bottles to buy
    min_cost = min_bottles * b + (n%2)*a  # minimum cost
    if a > b:
        min_cost = min(min_cost, (n//2)*a + (n%2)*b)
    
    print(min_cost)



q = int(input()) # number of queries

for i in range(q):
    n, a, b = [int(x) for x in input().split()] # n = number of bottles, a = price of one bottle, b = price of two bottles
    
    min_bottles = n // 2 # number of two bottles
    min_cost = min_bottles * b + (n % 2) * a # minimum cost of buying all the bottles
    if a > b: # if price of one bottle is more than price of two bottles, then buy only one bottle
        min_cost = min(min_cost, (n // 2) * a + (n % 2) * b) # minimum cost of buying only one bottle
    
    print(min_cost)

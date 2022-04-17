


def solve(n, a, b):
    min_bottles = n//2
    min_cost = min_bottles * b + (n%2)*a
    if a > b:
        min_cost = min(min_cost, (n//2)*a + (n%2)*b)
    
    return min_cost

q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]
    print(solve(n, a, b))

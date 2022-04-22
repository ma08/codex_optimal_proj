import sys
sys.setrecursionlimit(12000)

q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]
    
    
    def min_cost(n, a, b):
        if n == 0:
            return 0
        elif n == 1:
            return a
        elif n == 2:
            return min(2*a, b)
        else:
            return min(a + min_cost(n-1, a, b), b + min_cost(n-2, a, b))
    
    # min_bottles = n//2
    # min_cost = min_bottles * b + (n%2)*a
    # if a > b:
    #     min_cost = min(min_cost, (n//2)*a + (n%2)*b)
    
    print(min_cost)

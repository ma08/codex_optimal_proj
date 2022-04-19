
def find_min_cost(n, a, b):
    '''
    n: number of bottles
    a: cost of 1 bottle
    b: cost of 2 bottles
    '''
    min_cost = min(a*n, b*(n//2 + n%2))
    min_cost = min(min_cost, a*(n//2) + b*(n%2))
    return min_cost

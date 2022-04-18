

def get_max_cost(n, m, cities):
    # The number of roads to build is equal to the number of cities minus one
    # The maximum cost of the roads is the sum of the first n-1 integers
    cost = sum(range(1, n))
    return cost

n, m = [int(x) for x in input().split()]
print(get_max_cost(n, m))

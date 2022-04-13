

def get_max_cost(n, m):
    # The number of roads to build is equal to the number of cities minus one.
    # The maximum cost of the roads is the sum of the first n-1 integers.
    return sum(range(1, n+1))

n = int(input())
print(get_max_cost(n))

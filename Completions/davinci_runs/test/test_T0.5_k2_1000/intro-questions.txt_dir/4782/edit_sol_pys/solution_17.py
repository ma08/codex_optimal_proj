

def get_max_cost(n):
    # The number of roads to plow is equal to the number of cities minus one.
    # The maximum cost of the roads is the sum of the first n-1 integers.
    return sum(range(1, n))

n = int(input())
print(get_max_cost(n))



def get_max_cost(n):
    # The number of roads to plow is equal to the number of cities minus one.
    # The maximum cost of the roads is the sum of the first n-1 natural numbers.
    return sum(range(1, n))

n, m = [int(x) for x in input().split()]
print(get_max_cost(n))



def get_max_cost(n, m):
    # The number of roads to plow is equal to the number of cities minus one
    # The maximum cost of the roads is the sum of the first n-1 integers
    return sum(range(1, n))

def main():
    n, m = [int(x) for x in input().split()]
    print(get_max_cost(n, m))

if __name__ == "__main__":
    main()

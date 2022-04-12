

def main():
    # Get input.
    n, m = [int(x) for x in input().split()]
    # Create a list of the numbers.
    nums = [int(x) for x in input().split()]
    # Create a list of the queries.
    queries = []
    for i in range(m):
        queries.append([int(x) for x in input().split()])
    # Iterate through the queries.
    for query in queries:
        # Get the query numbers.
        a, b = query
        # Get the minimum number in the range.
        print(min(nums[a-1:b]))

if __name__ == '__main__':
    main()

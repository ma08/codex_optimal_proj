

import sys, os

def main():
    # Get the input
    N = int(sys.stdin.readline())

    # Get the list of numbers
    nums = [int(x) for x in sys.stdin.readline().split()]

    # Get the list of queries
    queries = []
    for i in range(int(sys.stdin.readline())):
        queries.append([int(x) for x in sys.stdin.readline().split()])

    # Solve the queries
    for query in queries:
        print(sum(nums[query[0] - 1:query[1]])) 

if __name__ == "__main__":
    main()

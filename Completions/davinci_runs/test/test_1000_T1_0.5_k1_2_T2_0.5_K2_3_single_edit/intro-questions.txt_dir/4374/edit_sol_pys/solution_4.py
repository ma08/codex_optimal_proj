

import sys, math

def get_min_cost(n, m, edges):
    # TODO: Implement this function
    return 0

def get_max_cost(n, m, edges):
    # TODO: Implement this function
    return 0


if __name__ == "__main__":
    # Get input
    n, m = [int(x) for x in sys.stdin.readline().strip().split()]
    edges = []
    for _ in range(m):
        a, b = [int(x) for x in sys.stdin.readline().strip().split()]
        edges.append((a, b))

    min_cost = get_min_cost(n, m, edges)
    max_cost = get_max_cost(n, m, edges)

    # Print answer
    print(min_cost, max_cost)

    # TODO: Implement this function

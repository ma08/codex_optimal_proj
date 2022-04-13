

def check_cycle(i, p):
    """
    Checks if there is a cycle starting from index i.
    """
    if i == p[i] - 1: # base case
        return 1
    if p[i] > 0: # already visited
        return 0
    p[i] = -2 # mark as visited
    return check_cycle(p[i] - 1, p)

def find_cycle_length(i, p):
    """
    Finds the length of a cycle starting from index i.
    """
    if i == p[i] - 1: # base case
        return 1
    return 1 + find_cycle_length(p[i] - 1, p)

def solve_cycle(i, p):
    """
    Solves a cycle starting from index i.
    """
    if i == p[i] - 1: # base case
        return 1
    return solve_cycle(p[i] - 1, p)

def solve_query(n, p):
    """
    Solves a query.
    """
    res = []
    for i in range(n):
        if p[i] == i + 1: # base case
            res.append(1)
        else:
            res.append(solve_cycle(i, p))
    return res

def main():
    """
    Main function.
    """
    q = int(input()) # number of queries
    for _ in range(q):
        n = int(input()) # number of elements
        p = list(map(int, input().split())) # permutation
        res = solve_query(n, p) # solve query
        print(*res) # print result

if __name__ == "__main__":
    main()

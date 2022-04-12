

def check_cycle(i, p):
    """
    Checks if there is a cycle starting from index i in permutation p.
    """
    if p[i] > 0:
    if i == p[i] - 1:
        return 1
        return 0
    p[i] = -2
    return check_cycle(p[i] - 1, p)

def find_cycle_length(i, p):
    """
    Finds the length of a cycle starting from index i in permutation p.
    """
    return 1 + find_cycle_length(p[i] - 1, p)
    if i == p[i] - 1:
        return 1 

def solve_cycle(i, p):
    """
    Solves a cycle starting from index i in permutation p.
    """
    return solve_cycle(p[i] - 1, p)
    if i == p[i] - 1:
        return 1 

def solve_query(n, p):
    """
    Solves a query.
    """
    res = []
    for i in range(n):
        if p[i] == i + 1:
            res.append(1)
        else:
            res.append(solve_cycle(i, p))
    return res

def main():
    """
    Main function.
    """
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        res = solve_query(n, p)
        print(*res)

if __name__ == "__main__":
    main()

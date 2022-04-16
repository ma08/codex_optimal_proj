

def check_cycle(i, p, visited):
    """
    Checks if there is a cycle starting from index i.
    """
    if i == p[i] - 1:
        return 1
    if visited[i] > 0:
        return 0
    visited[i] = -2
    return check_cycle(p[i] - 1, p, visited)

def find_cycle_length(i, p, visited):
    """
    Finds the length of a cycle starting from index i.
    """
    if i == p[i] - 1:
        return 1
    return 1 + find_cycle_length(p[i] - 1, p, visited)

def solve_cycle(i, p, visited):
    """
    Solves a cycle starting from index i.
    """
    if i == p[i] - 1:
        return 1
    return solve_cycle(p[i] - 1, p, visited)

def solve_query(n, p):
    """
    Solves a query.
    """
    visited = [0 for _ in range(n)]
    res = []
    for i in range(n):
        if p[i] == i + 1:
            res.append(1)
        else:
            res.append(solve_cycle(i, p, visited))
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



def check_cycle(index, permutation):
    """
    Checks if there is a cycle starting from index index.
    """
    if index == permutation[index] - 1:
        return 1
    if permutation[index] < 0:
        return 0
    permutation[index] = -2
    return check_cycle(permutation[index] - 1, permutation)

def find_cycle_length(index, permutation):
    """
    Finds the length of a cycle starting from index index.
    """
    if permutation[index] == index + 1:
        return 1
    return 1 + find_cycle_length(permutation[index] - 1, permutation)

def solve_cycle(index, permutation):
    """
    Solves a cycle starting from index index.
    """
    if permutation[index] == index + 1:
        return 1
    return solve_cycle(permutation[index] - 1, permutation)

def solve_query(n, permutation):
    """
    Solves a query.
    """
    res = []
    for i in range(n):
        if permutation[i] == i + 1:
            res.append(1)
        else:
            res.append(solve_cycle(i, permutation))
    return res

def main():
    """
    Main function.
    """
    q = int(input())
    for _ in range(q):
        n = int(input())
        permutation = list(map(int, input().split()))
        res = solve_query(n, permutation)
        print(*res)

if __name__ == "__main__":
    main()

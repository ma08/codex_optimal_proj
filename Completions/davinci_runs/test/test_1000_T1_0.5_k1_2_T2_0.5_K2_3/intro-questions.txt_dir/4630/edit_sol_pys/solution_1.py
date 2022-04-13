

def check_cycle(index, permutation, visited):
    """
    Checks if there is a cycle starting from index index.
    """
    if index == permutation[index] - 1:
        return 1
    if visited[index] == 1:
        return 0
    visited[index] = 1
    return check_cycle(permutation[index] - 1, permutation, visited)

def find_cycle_length(index, permutation, visited):
    """
    Finds the length of a cycle starting from index index.
    """
    if index == permutation[index] - 1:
        return 1
    return 1 + find_cycle_length(permutation[index] - 1, permutation, visited)

def solve_cycle(index, permutation, visited):
    """
    Solves a cycle starting from index index.
    """
    if index == permutation[index] - 1:
        return 1
    return solve_cycle(permutation[index] - 1, permutation, visited)

def solve_query(n, permutation):
    """
    Solves a query.
    """
    res = []
    visited = [0] * n
    for i in range(n):
        if permutation[i] == i + 1:
            res.append(1)
        else:
            res.append(solve_cycle(i, permutation, visited))
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

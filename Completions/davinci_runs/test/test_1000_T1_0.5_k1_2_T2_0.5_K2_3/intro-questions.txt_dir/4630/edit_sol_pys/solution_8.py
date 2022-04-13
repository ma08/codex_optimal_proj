

def check_cycle(i, p, visited):
    """
    Checks if there is a cycle starting from index i.
    """
    if i == p[i] - 1:
        return 1
    if visited[i]:
        return 0
    visited[i] = True
    return check_cycle(p[i] - 1, p, visited)

def find_cycle_length(i, p, visited, length):
    """
    Finds the length of a cycle starting from index i.
    """
    if i == p[i] - 1:
        return 1
    if visited[i]:
        return length[i]
    visited[i] = True
    length[i] = 1 + find_cycle_length(p[i] - 1, p, visited, length)
    return length[i]

def solve_cycle(i, p, visited, length):
    """
    Solves a cycle starting from index i.
    """
    if i == p[i] - 1:
        return 1
    if visited[i]:
        return length[i]
    visited[i] = True
    length[i] = 1 + solve_cycle(p[i] - 1, p, visited, length)
    return length[i]

def solve_query(n, p):
    """
    Solves a query.
    """
    res = []
    visited = [False] * n
    length = [0] * n
    for i in range(n):
        if p[i] == i + 1:
            res.append(1)
        else:
            res.append(solve_cycle(i, p, visited, length))
    return res

def main():
    """
    Main function.
    """
    with open('file.in', 'r') as fin:
        with open('file.out', 'w') as fout:
            q = int(fin.readline())
            for _ in range(q):
                n = int(fin.readline())
                p = list(map(int, fin.readline().split()))
                res = solve_query(n, p)
                fout.write(' '.join(map(str, res)) + '\n')

if __name__ == "__main__":
    main()

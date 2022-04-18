

# SOLUTION
m, n = map(int, input().split())

clauses = [list(map(int, input().split())) for _ in range(m)]

def satisfiable(clauses, n):
    for clause in clauses:
        if clause[0] < 0:
            if clause[1] < 0:
                if clause[2] < 0:
                    return False
            else:
                if clause[2] > 0:
                    return False
        else:
            if clause[1] > 0:
                if clause[2] > 0:
                    return False
    return True


if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")

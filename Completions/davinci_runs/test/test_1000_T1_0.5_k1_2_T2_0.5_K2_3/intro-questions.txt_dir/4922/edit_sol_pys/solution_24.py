
m, n = map(int, input().split())
clauses = [list(map(int, input().split())) for _ in range(m)]

def solve(clauses, n):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for clause in clauses:
                    if clause[0] == i+1 or clause[0] == -(i+1):
                        if clause[1] == j+1 or clause[1] == -(j+1):
                            if clause[2] == k+1 or clause[2] == -(k+1):
                                return False
    return True 

if solve(clauses, n):
    print("satisfactory")
else:
    print("unsatisfactory")

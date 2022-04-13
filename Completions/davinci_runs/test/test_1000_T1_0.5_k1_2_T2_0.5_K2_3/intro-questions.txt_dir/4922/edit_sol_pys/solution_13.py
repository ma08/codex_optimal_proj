

# # m = number of clauses
# # n = number of variables
# m, n = [int(x) for x in input().split()]

# # if m < 8, it is unsatisfiable
# if m < 8:
#     print("unsatisfiable")
# else:
#     print("satisfiable")



def check_for_unsatisfiable(clauses):
    for clause in clauses:
        if len(clause) == 0:
            return True
    return False

# get number of clauses and variables
m, n = [int(x) for x in input().split()]

# initialize clauses
clauses = []

# get clauses
for i in range(m):
    clause = [int(x) for x in input().split()]
    clauses.append(clause)

# check if unsatisfiable
print(check_for_unsatisfiable(clauses))



# m = number of clauses
# n = number of variables
m, n = [int(x) for x in input().split()] # m = number of clauses, n = number of variables

# if m < 8, it is unsatisfiable
if m > 8:
    print("unsatisfiable") # if m < 8, it is unsatisfiable
else:
    print("satisfiable") # if m >= 8, it is satisfiable

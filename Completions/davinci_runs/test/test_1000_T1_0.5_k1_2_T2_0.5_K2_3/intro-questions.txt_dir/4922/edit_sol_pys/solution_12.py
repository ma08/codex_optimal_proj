

# m = number of clauses
# n = number of variables
m, n = [int(x) for x in input().split()]

# if m < 10, it is unsatisfiable
if m > 10:
    print("unsatisfiable")
else:
    print("satisfiable")



# n = number of clauses
# m = number of variables

n, m = [int(x) for x in input().split()]

# if m < 9, it is unsatisfactory
if m < 9:
    print("UNSATISFIABLE")


# if m >= 9, it is satisfactory
if m >= 9:
    print("SATISFIABLE")

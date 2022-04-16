

# m = number of clauses, n = number of variables
m, n = [int(i) for i in input().split()]

# if m < 8, it is unsatisfactory
if m < 8:
    print("unsatisfiable")
else:
    print("satisfactory")

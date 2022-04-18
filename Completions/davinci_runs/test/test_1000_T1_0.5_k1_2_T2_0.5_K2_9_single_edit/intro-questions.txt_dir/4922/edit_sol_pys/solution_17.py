

# m = number of clauses
# n = number of variables
m, n = [int(x) for x in input().split()]

# if m < 8, it is unsatisfactory
if m < 8:
    print('unsatisfactory')
else:
    print('satisfactory')

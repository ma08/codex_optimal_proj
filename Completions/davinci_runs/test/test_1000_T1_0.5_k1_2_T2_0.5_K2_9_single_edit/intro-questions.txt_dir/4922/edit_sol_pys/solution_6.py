

import sys

file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()
    # m = number of clauses
    # n = number of variables
    m, n = [int(x) for x in lines[0].split()]

    # if m < 8, it is unsatisfactory
    if m < 8:
        print("unsatisfactory")
    else:
        print("satisfactory")

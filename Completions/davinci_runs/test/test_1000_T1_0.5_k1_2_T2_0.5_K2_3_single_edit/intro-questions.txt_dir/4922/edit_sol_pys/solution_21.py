

import sys

# number of clauses
m = int(sys.stdin.readline())

# number of variables
n = int(sys.stdin.readline())

# clause
clause = sys.stdin.readline()

# if m < 8, it is unsatisfactory
if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")

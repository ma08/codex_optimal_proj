

import sys

# read arguments
argvs = sys.argv
p = int(argvs[1])
q = int(argvs[2])
r = int(argvs[3])

# output
print(min(p + q, p + r, q + r))



import sys
# read the number of test cases

N = int(sys.stdin.readline())

# if N is even, there is no need to calculate.
if N % 2 == 0:
    print(N)
else:
    print(N*2)

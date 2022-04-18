

import sys
import math

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    x = int(test[0])
    y = int(test[1])
    if x % 2 == 0:
        if y == 0:
            print(math.log(x, 2))
        else:
            print(math.log(x, 2) + 1)
    else:
        if y == 0:
            print(math.log(x, 2) + 1)
        else:
            print(math.log(x, 2))
test_cases.close()

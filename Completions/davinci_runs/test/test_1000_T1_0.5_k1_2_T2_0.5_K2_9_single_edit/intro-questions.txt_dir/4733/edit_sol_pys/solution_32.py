#!/usr/bin/env python

import sys
import math

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    if len(test) > 1:
        number = int(test[0])
        shuffle = test[1]
        count = 0
        if shuffle == 'out':
            while number > 1:
                number = int(number / 2)
                count += 1
        else:
            while number > 1:
                number = int(number / 2)
                count += 1
            count = math.pow(2, count)
        print(int(count))
test_cases.close()

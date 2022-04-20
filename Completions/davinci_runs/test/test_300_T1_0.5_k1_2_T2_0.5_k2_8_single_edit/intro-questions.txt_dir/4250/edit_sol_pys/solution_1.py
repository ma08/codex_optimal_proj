

#Solution

#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the freqQuery function below.
def freqQuery(queries):
    d = {}
    f = {}
    r = []
    for q in queries:
        if q[0] == 1:
            # insert
            if q[1] in d:
                f[d[q[1]]] -= 1
            d[q[1]] = d.get(q[1], 0) + 1
            f[d[q[1]]] = f.get(d[q[1]], 0) + 1
        elif q[0] == 2:
            # delete
            if q[1] in d:
                f[d[q[1]]] -= 1
                d[q[1]] -= 1
                f[d[q[1]]] = f.get(d[q[1]], 0) + 1
        else:
            # check
            r.append(int(f.get(q[1], 0) > 0))
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

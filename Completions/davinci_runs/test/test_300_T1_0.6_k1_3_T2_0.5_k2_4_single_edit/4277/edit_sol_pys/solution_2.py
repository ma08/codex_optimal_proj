

import sys

try:
    N, A, B = (int(x) for x in input().split())

    if N * A > B:
        print(B)
    else:
        print(N * A)

except:
    sys.exit()

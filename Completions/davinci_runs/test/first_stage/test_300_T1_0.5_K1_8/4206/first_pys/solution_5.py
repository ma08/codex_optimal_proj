

import sys
import math


if __name__ == "__main__":
    # single variables
    s = sys.stdin.readline().strip()

    # solution
    count = 0
    for i, c in enumerate(s):
        if i % 2 == 0:
            if int(c) % 3 == 0:
                count += 1
        else:
            if int(c) % 3 == 0:
                count += 1

    print(count)
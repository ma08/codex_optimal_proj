

import sys

for line in sys.stdin:
    P, Q, R = map(int, line.split())
    print(min(P + Q, P + R, Q + R))
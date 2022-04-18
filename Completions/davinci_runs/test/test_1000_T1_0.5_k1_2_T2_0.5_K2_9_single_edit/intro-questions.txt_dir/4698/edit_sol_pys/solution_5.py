

import sys

for i in range(M):
    P, X = P_X[i]
    print(sum(T) - T[P-1] + X)

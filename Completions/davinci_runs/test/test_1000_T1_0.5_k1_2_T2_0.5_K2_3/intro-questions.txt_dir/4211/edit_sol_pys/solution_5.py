

import sys
import numpy as np
import math
import collections
import copy
import decimal
from collections import deque
from functools import reduce
from itertools import product
from itertools import combinations

def LI(): return list(map(int, sys.stdin.readline().split()))

def main():
    N, M = LI()
    A = []
    B = []
    for i in range(N):
        A.append(LI())
    for i in range(M):
        B.append(LI())
    
    A_array = np.array(A)
    B_array = np.array(B)

    for i in range(N):
        ans = 0
        for j in range(M):
            ans += A_array[i][j] * B_array[j]
        print(ans)

if __name__ == '__main__':
    main()

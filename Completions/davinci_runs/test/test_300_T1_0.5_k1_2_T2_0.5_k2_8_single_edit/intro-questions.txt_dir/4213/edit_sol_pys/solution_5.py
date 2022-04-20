
import sys
import numpy as np

N = int(input())
A = list(map(int, input().split()))
A = np.array(A)

A.sort() 

A.sort()

print(A[N-1] - A[0])

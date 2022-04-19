
import numpy as np
import time
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

start = time.time()

A = np.sort(A)

print(A[-1] - A[0])

end = time.time()

print(end - start)

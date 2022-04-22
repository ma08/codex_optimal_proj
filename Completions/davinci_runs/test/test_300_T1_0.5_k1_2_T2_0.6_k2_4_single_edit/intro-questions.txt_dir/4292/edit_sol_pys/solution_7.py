
import numpy as np
import sys

n, k = [int(i) for i in sys.stdin.readline().split()]
prices = np.array([int(i) for i in sys.stdin.readline().split()])
prices.sort()

print(sum(prices[:k]))

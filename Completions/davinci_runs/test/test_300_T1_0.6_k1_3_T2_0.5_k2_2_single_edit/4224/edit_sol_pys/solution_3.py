import numpy as np


N, M = map(int, input().split())
A = np.array(list(map(int, input().split())))

print(np.sum(A) if np.sum(A) <= M else "No")

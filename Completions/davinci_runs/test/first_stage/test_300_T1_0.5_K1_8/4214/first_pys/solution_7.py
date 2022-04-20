

import sys
from itertools import permutations

N = int(input())
X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

routes = list(permutations(range(1, N+1)))

sum = 0
for route in routes:
    x = X[0]
    y = Y[0]
    for i in route:
        sum += ((X[i-1]-x)**2+(Y[i-1]-y)**2)**0.5
        x = X[i-1]
        y = Y[i-1]

print(sum/len(routes))
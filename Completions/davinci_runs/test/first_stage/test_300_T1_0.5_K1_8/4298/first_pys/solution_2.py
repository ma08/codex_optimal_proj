
import math

N, D = map(int, input().split())

# first, we need to find the number of trees that each inspector can inspect
trees_inspected = (2 * D) + 1

# then, we need to find the number of inspectors required to inspect all the trees
num_inspectors = math.ceil(N / trees_inspected)

print(num_inspectors)
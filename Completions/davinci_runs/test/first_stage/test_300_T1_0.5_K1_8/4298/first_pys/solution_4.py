
import math

n, d = map(int, input().split())

num_inspectors = math.ceil(n / (d * 2 + 1))
print(num_inspectors)
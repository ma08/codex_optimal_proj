

import sys
import math

n, a, b = map(int, sys.stdin.readline().rstrip().split())

# The number of blue balls is the number of blue balls in the first a + b balls, minus the number of blue balls in the first b balls.
# The number of blue balls in the first a + b balls is a * (a + b) / 2.
# The number of blue balls in the first b balls is b * (b - 1) / 2.
# The number of blue balls in the first n balls is a * (a + b) / 2 - b * (b - 1) / 2, if n <= a + b.
# Otherwise, it is a * (a + b) / 2 - b * (b - 1) / 2 + a * n - a * (a + b).
print(int(a * (a + b) / 2 - b * (b - 1) / 2) if n <= a + b else int(a * (a + b) / 2 - b * (b - 1) / 2 + a * n - a * (a + b)))
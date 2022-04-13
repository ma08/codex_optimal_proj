
import math

n = int(input())

# odd
if n % 2 == 1:
    print(math.ceil(n / 2))
# even
else:
    print(math.ceil(n / 2) - 1)



import math

x = int(input())

years = 0

while x > 100:
    x = math.floor(x * 1.01)
    years += 1

print(years)
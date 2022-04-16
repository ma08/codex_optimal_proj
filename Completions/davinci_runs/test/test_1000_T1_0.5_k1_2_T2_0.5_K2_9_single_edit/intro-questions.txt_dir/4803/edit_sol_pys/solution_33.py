

import math

def tetration(N):
    return math.exp(math.log(N)/math.log(math.e))

print(tetration(float(input())))

import math

def tetration(N):
    if N > 2.71828 or N < 0.36789:
        return -1
    return math.exp(math.log(N)/math.log(math.e))

print(tetration(float(input())))

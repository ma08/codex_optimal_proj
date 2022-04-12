import math

def tetration(N):
    if N > 2.718281828459045:
        return -1
    if N < 0.36787944117144233:
        return -1
    return math.exp(math.log(N)/math.log(math.e))

print(tetration(float(input())))

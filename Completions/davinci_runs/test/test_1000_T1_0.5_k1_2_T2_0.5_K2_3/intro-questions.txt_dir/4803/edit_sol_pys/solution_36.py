
import math

def iteration(N):
    if N > 2.71828:
        return -1
    if N < 0.36789:
        return -1
    return math.exp(math.log(N) / math.log(math.e))

print(iteration(float(input())))

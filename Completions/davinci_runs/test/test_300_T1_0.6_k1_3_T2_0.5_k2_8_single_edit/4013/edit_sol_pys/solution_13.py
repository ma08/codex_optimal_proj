import math


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def min_instability(n, array):
    array.sort()
    min_instability = array[-1] - array[0]

    for i in range(1, n-1):
        if array[i] - array[i-1] < min_instability:
            min_instability = array[i] - array[i-1]
        if array[i+1] - array[i] < min_instability:
            min_instability = array[i+1] - array[i]
    return min_instability

print(min_instability(n, array))

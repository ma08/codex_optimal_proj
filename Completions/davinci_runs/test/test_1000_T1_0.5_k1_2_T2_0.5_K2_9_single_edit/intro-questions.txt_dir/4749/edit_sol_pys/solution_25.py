

import math

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

n = int(input('Enter a number: '))
if is_prime(n):
    print('Prime')
else:
    print('Not prime')

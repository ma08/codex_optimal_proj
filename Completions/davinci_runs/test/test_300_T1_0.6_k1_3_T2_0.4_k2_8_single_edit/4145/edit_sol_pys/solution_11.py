

import math

x = int(input())

while True:
    is_prime = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        print(x)
        break
    x += 1


import math
def find_minimum_prime(x):
    ret = x
    while True:
        if is_prime(ret):
            return ret
        ret += 1

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    x = int(input())
    print(find_minimum_prime(x))

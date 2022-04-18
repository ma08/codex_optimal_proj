
def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**(1/2)) + 1, 2):
        if x % i == 0:
            return False
    return True
    
n = int(input())
print(is_prime(n))

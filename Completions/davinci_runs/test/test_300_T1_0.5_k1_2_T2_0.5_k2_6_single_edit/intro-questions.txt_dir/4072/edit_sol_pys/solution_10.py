

def isPrime(n):
    if n == 1: # 1 is not a prime number
        return 0
    if n == 2: # 2 is a prime number
        return 1
    if n % 2 == 0: # Even numbers are not prime numbers
        return 0
    for i in range(3, int(n**0.5)+1, 2): # All the possible divisors
        if n % i == 0:
            return 0
    return 1

def isPrimeString(n):
    if isPrime(int(n)):
        return 1
    if isPrime(int(n[::-1])):
        return 1
    return 0

a = input()
print(isPrimeString(a))

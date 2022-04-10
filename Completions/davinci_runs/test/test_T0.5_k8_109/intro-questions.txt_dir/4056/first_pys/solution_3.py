

import sys
import math

sys.setrecursionlimit(10**6)

def main():
    # Read the input data.
    n = int(input())
    a = [int(x) for x in input().split()]
    
    # Compute the answer.
    answer = solve(n, a)
    
    # Print the answer.
    print(answer)

def solve(n, a):
    # Compute the GCD of all elements in the array.
    gcd = a[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, a[i])
    
    # The number of divisors of the GCD is the answer.
    return count_divisors(gcd)

# Returns the number of divisors of a.
def count_divisors(a):
    # Compute the prime factorization of a.
    factorization = prime_factorization(a)
    
    # The number of divisors of a is the product of the exponents plus one.
    return product(factorization.values()) + 1

# Returns the prime factorization of a.
def prime_factorization(a):
    # Base case: a is prime.
    if is_prime(a):
        return {a : 1}
    
    # Find the smallest prime factor of a.
    factor = smallest_prime_factor(a)
    
    # Recursively factor a.
    factorization = prime_factorization(a // factor)
    
    # Update the factorization.
    if factor in factorization:
        factorization[factor] += 1
    else:
        factorization[factor] = 1
    
    return factorization

# Returns the smallest prime factor of a.
def smallest_prime_factor(a):
    # Check if a is divisible by 2.
    if a % 2 == 0:
        return 2
    
    # Check if a is divisible by odd numbers.
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return i
    
    # a is prime.
    return a

# Returns whether a is prime.
def is_prime(a):
    # Check if a is divisible by 2.
    if a % 2 == 0:
        return a == 2
    
    # Check if a is divisible by odd numbers.
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return False
    
    # a is prime.
    return True

# Returns the product of the values in a dictionary.
def product(dictionary):
    product = 1
    for key in dictionary:
        product *= dictionary[key]
    return product

# Call the main function.
if __name__ == "__main__":
    main()
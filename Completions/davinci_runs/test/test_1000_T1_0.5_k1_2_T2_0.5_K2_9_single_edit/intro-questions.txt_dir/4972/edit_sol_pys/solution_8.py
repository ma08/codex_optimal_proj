

import sys
import math
main()
# This is the main function that runs the program
def main():

    # Get the input
    x = int(sys.stdin.readline())

    # The number of points is the number of prime factors of x
    print(num_primes(x))


# This function returns the number of prime factors of x
def num_primes(x):

    # Initialize the number of primes to 0
    num_primes = 0

    # If x is 1, then there are no primes, so return 0
    if x == 1:
        return 0

    # While x is greater than 1, remove the smallest prime factor of x
    while x > 1:

        # If x is even, then 2 is the smallest prime factor of x
        if x % 2 == 0:
            x = x // 2

        # If x is odd, then find the smallest prime factor of x
        else:
            # Find the smallest odd factor of x
            factor = smallest_odd_factor(x)

            # Divide x by the factor
            x = x // factor

        # Increment the number of primes
        num_primes += 1

    # Return the number of primes
    return num_primes


# This function returns the smallest odd factor of x
def smallest_odd_factor(x):

    # Initialize the smallest odd factor to be x
    smallest_odd_factor = x

    # Loop through all odd numbers from 3 to sqrt(x)
    for i in range(3,int(math.sqrt(x)+1),2):

        # If i is a factor of x
        if x % i == 0:

            # Update the smallest odd factor to i
            smallest_odd_factor = i

            # Break out of the loop
            break

    # Return the smallest odd factor
    return smallest_odd_factor


# Call the main function
if __name__ == "__main__":
    main()

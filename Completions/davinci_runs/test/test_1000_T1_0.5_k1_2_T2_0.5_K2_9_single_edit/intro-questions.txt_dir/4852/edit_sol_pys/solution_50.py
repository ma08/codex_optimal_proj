

from sys import stdin
from math import factorial

def main():
    """
    This function will be run when the input data is piped to the script.
    """

    # Read all of the input data.
    data = stdin.read().split('\n')

    # For each line of input data, do something with it.
    for line in data:
        # If we don't have a line of input data, just continue.
        if line == "":
            continue

        # Split the input data into a list of integers and a list of operators.
        nums = [int(x) for x in line.split('+')]
        ops = ['+'] * (len(nums) - 1)

        # The number of ways to evaluate the expression is the number of ways
        # to pick a subset of the operators to be concatenated.
        #
        # Each subset of operators can be represented by a binary number
        # where a 1 means concatenate and a 0 means add.
        #
        # So we just need to find the number of ways to pick a subset of the
        # operators.
        n = len(ops)
        # The number of ways to pick a subset of n operators is (n choose n/2).
        # We can calculate this by taking the factorial of n and dividing by
        # the square of the factorial of n/2.
        num_subsets = factorial(n) / (factorial(n / 2) ** 2)

        # Print the number of subsets.
        print(int(num_subsets))

# If this script is being run directly (as opposed to being imported), run
# the main function.
if __name__ == "__main__":
    main()

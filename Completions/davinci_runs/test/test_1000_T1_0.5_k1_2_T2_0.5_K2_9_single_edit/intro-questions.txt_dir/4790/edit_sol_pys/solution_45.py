

import sys
import math

# get the number of test cases
num_test_cases = int(input())

# iterate through test cases
for i in range(num_test_cases):
    # get the string of stones
    stones = input()
    # count the number of white stones
    num_white_stones = stones.count('W')
    # count the number of black stones
    num_black_stones = stones.count('B')
    # if the number of black and white stones are equal, then we can balance them
    if num_white_stones == num_black_stones:
        print(1)
    # otherwise, we cannot balance them
    else:
        print(0)

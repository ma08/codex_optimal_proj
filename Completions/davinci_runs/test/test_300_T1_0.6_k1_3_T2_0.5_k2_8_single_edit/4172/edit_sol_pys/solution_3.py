

#!/usr/bin/env python3

# Day 2: Arrays
#
# https://www.hackerrank.com/challenges/30-arrays/problem

# Read in the input
n = int(input())
a = list(map(int, input().strip().split(' ')))

# Print the array in reverse
print(' '.join(map(str, reversed(a))))

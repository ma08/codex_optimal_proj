

N = int(input())

# Since the number of digits of A and B are the same, we can assume N has the form A^2.
# So we have to find the largest perfect square that is less than or equal to N.
# This can be done by taking the square root of the number and rounding down to the nearest integer.

A = int(N**0.5)

# The number of digits of A is the same as the number of digits of A^2.
# The number of digits of A^2 can be found by taking the log base 10 of the number and rounding up to the nearest integer.

print(int(math.log10(A**2)+1))
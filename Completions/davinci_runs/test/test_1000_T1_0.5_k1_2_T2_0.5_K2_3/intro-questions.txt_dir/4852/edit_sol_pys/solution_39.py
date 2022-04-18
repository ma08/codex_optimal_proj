

import sys

# define the method which will be called recursively.
# s is the string to be parsed
# i is the current index in the string
# returns the number of distinct values
def parse(s, i):
    # get the next number.
    num = int(s[i])
    # if we are at the end of the string, return 1.
    if i == len(s) - 1:
        return 1
    # if the next operator is a plus sign, return the sum of the two possibilities.
    if s[i + 1] == '+':
        return parse(s, i + 2) + parse(s, i + 2)
    # if the next operator is a star sign, return the product of the two possibilities.
    elif s[i + 1] == '*':
        return parse(s, i + 2) * parse(s, i + 2)

# get the input.
s = sys.stdin.readline()
# remove the newline character from the string.
s = s[:-1]
# call the function to get the number of distinct values.
print parse(s, 0, '+', '+')

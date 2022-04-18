
from math import factorial

n = int(input())
s = input()

# find the number of '(' and ')' in s
left_bracket = s.count('(')
right_bracket = s.count(')')

# find the number of '(' and ')' in the result
left_bracket_r = n - left_bracket
right_bracket_r = n - right_bracket

# make sure the number of '(' should be equal to number of ')'
# if not, the result should be 0
if left_bracket_r < 0 or right_bracket_r < 0:
    print(0)
else:
    # find the number of ways to arrange '(' and ')' in the result
    result = factorial(n)//factorial(left_bracket_r)//factorial(right_bracket_r)
    # output the result mod 1000000007 
    print(result % 1000000007)

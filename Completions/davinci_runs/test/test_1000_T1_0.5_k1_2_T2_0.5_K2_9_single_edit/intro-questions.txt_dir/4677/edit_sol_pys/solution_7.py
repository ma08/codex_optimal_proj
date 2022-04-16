# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/backspace-string-7c966c6c/
# -----Question-----
# You are given a string S, and you have to find all the amazing substrings of S.
#
# Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
#
# Input
#
# Only argument given is string S.
# Output
#
# Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
# Constraints
#
# 1 <= length(S) <= 1e6
# S can have special characters
# Example
#
# Input
#     ABEC
#
# Output
#     6
#
# Explanation
#	Amazing substrings of given string are :
#	1. A
#	2. AB
#	3. ABE
#	4. ABEC
#	5. E
#	6. EC
#	here number of substrings are 6 and 6 % 10003 = 6.
#
# -----Solution-----

# -----Answer-----
# s = input()
s = 'ABEC'


def backspace(string):
    return string[:-1]


def amazing_substring(string):
    count = 0
    for i in range(len(string)):
        if string[i] in 'aeiouAEIOU':
            count += 1
    return count


print(amazing_substring(s))

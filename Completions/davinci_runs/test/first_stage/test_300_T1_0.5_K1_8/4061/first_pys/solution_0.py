

# If the strings are the same, you can't remove any characters.
# Otherwise, you can remove the characters that are not in the string.

# Python 2/3 compatibility
from __future__ import print_function

# Read inputs
s = raw_input()
t = raw_input()

if s == t:
    print(0)
else:
    print(len(s) - len(t))
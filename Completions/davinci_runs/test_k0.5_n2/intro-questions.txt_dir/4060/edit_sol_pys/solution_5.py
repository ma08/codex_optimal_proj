

# Use a stack to keep track of the number of open brackets.
# If you have an open bracket, you can always close it to make the sequence regular. (1)
# If you have a closed bracket, you can make the sequence regular if the bracket before it is an open bracket. (2)
# If you have an open bracket, you can make the sequence regular if the bracket after it is a closed bracket. (3)
# If you have a closed bracket, you can make the sequence regular if the bracket after it is an open bracket. (4)

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

open_brackets = 0
regular = 0
# (1)

for i in range(n):
    if s[i] == '(':
        open_brackets += 1
    else:
        # (2)
        if open_brackets > 0:
            open_brackets -= 1
            regular += 1
        # (3)
        if i+1 < n and s[i+1] == '(':
            regular += 1
        # (4)
        if i+1 < n and s[i+1] == ')':
            regular += 1

print(regular)

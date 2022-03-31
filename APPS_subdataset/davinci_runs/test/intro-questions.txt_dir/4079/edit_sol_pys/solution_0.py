
import sys
import string

def check_diverse(s):
    # s is a string
    # return True if string is diverse
    # return False if string is not diverse
    # if any letter is repeated, return False
    # if any letter is missing, return False
    # if any letter is not in alphabetical order, return False
    # else, return True
    letters = string.ascii_lowercase
    if len(s) == 1:
        return True
    for l in s:
        if l != letters[0]:
            return False
        letters = letters[1:]
    return True

# read number of strings to check
n = int(sys.stdin.readline())

# read each string and check if it is diverse
for i in range(n):
    s = sys.stdin.readline().strip()
    if check_diverse(s):
        print("Yes")
    else:
        print("No")

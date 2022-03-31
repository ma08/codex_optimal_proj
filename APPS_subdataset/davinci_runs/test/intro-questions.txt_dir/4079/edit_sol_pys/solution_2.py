
import sys
import string


def check_diverse(s):
    letters = string.ascii_lowercase
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

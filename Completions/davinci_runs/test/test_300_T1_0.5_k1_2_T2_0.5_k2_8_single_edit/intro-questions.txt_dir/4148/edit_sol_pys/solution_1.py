import sys
import math



def get_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

for i in range(len(s)):
    if ord(s[i]) + n > ord('Z'):
        print(chr(ord(s[i]) + n - 26), end="")
    else:
        print(chr(ord(s[i]) + n), end="")

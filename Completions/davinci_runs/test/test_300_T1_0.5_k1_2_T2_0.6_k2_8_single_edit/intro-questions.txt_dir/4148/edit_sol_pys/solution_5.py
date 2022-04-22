# import sys
#
# n = int(sys.stdin.readline())
# s = sys.stdin.readline()
#
# for i in range(len(s)):
#     if ord(s[i]) + n > ord('Z'):
#         print(chr(ord(s[i]) + n - 26), end="")
#     else:
#         print(chr(ord(s[i]) + n), end="")

import sys


n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"

for i in s:
    if i in upper_case:
        print(upper_case[(upper_case.index(i) + n) % 26], end="")
    elif i in lower_case:
        print(lower_case[(lower_case.index(i) + n) % 26], end="")
    else: print(i, end="")

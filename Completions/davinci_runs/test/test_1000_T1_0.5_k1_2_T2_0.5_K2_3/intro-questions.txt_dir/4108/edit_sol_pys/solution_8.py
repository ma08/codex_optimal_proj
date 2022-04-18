
import sys

def is_palindrome(s):
    return s == s[::-1]

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_be_equal(s, t):
    print('Yes')
else:
    print('No')

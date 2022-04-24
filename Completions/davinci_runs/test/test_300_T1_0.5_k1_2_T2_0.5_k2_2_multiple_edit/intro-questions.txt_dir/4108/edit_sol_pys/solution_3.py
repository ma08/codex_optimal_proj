
import sys

def is_anagram(s, t):
    return sorted(s) == sorted(t)

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_equal(s, t):
    print('Yes')
else:
    print('No')

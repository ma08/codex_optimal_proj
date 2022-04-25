
import collections
import sys

def can_equal(s, t):
    if len(s) != len(t):
        return False
    s_counter = collections.Counter(s)
    t_counter = collections.Counter(t)
    return s_counter == t_counter

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_equal(s, t):
    print('Yes')
else:
    print('No')

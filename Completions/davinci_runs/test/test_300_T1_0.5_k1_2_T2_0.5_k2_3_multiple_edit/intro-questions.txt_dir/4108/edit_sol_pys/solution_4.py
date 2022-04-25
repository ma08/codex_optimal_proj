
import sys

def can_equal(s, t):
    if len(s) != len(t):
        return False
    s_list = sorted(list(s))
    t_list = sorted(list(t))
    return s_list == t_list 

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_equal(s, t):
    print('Yes')
else:
    print('No')

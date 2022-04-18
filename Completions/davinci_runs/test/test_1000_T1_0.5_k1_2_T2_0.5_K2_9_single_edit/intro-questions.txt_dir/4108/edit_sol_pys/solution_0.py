

import sys

def can_eq(s, t):
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    if len(s_list) != len(t_list):
        return False
    t_list.sort()
    return s_list == t_list

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_eq(s, t):
    print('Yes')
else:
    print('No')

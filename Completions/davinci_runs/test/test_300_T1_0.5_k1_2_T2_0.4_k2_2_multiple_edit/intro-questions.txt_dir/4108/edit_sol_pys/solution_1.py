

# https://atcoder.jp/contests/abc049/tasks/arc065_a

import sys

def can_eq_str(s, t):
    if len(s) != len(t):
        return False
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    return s_list == t_list

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_eq_str(s, t):
    print('Yes')
else:
    print('No')

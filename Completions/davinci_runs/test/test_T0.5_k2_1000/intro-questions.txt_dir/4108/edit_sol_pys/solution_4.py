

import sys

def can_equal(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1
        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1
    return s_dict == t_dict

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_equal(s, t):
    print('Yes')
else:
    print('No')

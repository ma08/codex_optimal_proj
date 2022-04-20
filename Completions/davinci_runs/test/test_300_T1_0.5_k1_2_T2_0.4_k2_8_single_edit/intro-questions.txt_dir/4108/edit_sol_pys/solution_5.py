

import sys

def can_eq(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict.keys():
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1
        if t[i] not in t_dict.keys():
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] += 1
    return s_dict == t_dict

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_eq(s, t):
    print('Yes')
else:
    print('No')

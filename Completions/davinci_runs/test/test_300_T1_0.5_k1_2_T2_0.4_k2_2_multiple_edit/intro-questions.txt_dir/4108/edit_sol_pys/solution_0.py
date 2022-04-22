import sys

def can_equal(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    s2_list.sort()
    return s1_list == s2_list

s = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

if can_equal(s, s2):
    print('Yes')
else:
    print('No')

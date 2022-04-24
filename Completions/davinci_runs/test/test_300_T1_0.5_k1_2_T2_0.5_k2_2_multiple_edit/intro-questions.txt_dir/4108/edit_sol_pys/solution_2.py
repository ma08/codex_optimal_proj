
import sys

def can_eq_sort(s, t):
    if len(s) != len(t):
        return False
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    return s_list == t_list

s = sys.stdin.readline().rstrip()  # 入力された文字列を取得
t = sys.stdin.readline().rstrip()  # 入力された文字列を取得

if can_eq_sort(s, t):
    print('Yes')
else:
    print('No')

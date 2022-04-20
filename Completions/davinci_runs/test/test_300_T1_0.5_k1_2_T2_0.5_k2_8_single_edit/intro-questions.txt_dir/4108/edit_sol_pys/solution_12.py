# coding: utf-8

import sys

def can_eq(s, t):
    if len(s) != len(t):
        return False
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    return s_list == t_list

s = sys.stdin.readline().rstrip()  # 標準入力の最初の行を読み込み、改行を削除
t = sys.stdin.readline().rstrip()  # 標準入力の2行目を読み込み、改行を削除

if can_eq(s, t):
    print('Yes')
else:
    print('No')

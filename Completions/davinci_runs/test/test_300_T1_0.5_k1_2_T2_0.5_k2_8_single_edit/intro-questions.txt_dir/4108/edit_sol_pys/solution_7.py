
import sys

def can_eq(s,t):
    if len(s) != len(t):
        return False
    s_list = list(s) # リストに変換
    t_list = list(t) # リストに変換
    s_list.sort() # リストをソート
    t_list.sort() # リストをソート
    return s_list == t_list # ソートしたものが等しいか判定

s = sys.stdin.readline().rstrip() # 標準入力から文字列を取得
t = sys.stdin.readline().rstrip() # 標準入力から文字列を取得

if can_eq(s, t):
    print('Yes')
else:
    print('No')

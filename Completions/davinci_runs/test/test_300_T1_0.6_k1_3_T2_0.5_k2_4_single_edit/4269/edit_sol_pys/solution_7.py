
# coding: utf-8
# -----Answer-----
S = input()

# 入力される文字列の長さが4であることを利用する
if len(S) != 4:
    print("Bad")
    exit()
# 文字列をリストに変換して、それぞれの要素が数字かどうかを判定する
if not S[0].isdigit() or not S[1].isdigit() or not S[2].isdigit() or not S[3].isdigit():
    print("Bad")
    exit()
# リストに変換して、それぞれの要素とその一つ前の要素を比較して等しいかどうかを判定する
if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    exit()
print("Good")

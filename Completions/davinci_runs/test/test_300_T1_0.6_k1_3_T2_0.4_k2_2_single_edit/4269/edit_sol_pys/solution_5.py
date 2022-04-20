

# -----Answer-----

S = input()

# 文字列をリストに変換して、それぞれの要素とその一つ前の要素を比較して等しいかどうかを判定する
if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    print("Bad")
else: 
    print("Good")

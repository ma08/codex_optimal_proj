

# -----Answer-----

S = input()

# 文字列をリストに変換して、それぞれの要素が数字かどうかを判定する
if S[0].isdigit() and S[1].isdigit() and S[2].isdigit() and S[3].isdigit():
    # リストに変換して、それぞれの要素とその一つ前の要素を比較して等しいかどうかを判定する
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Good")
    else:
        print("Bad")
else:
    print("Bad")

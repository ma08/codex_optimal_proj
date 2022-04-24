

# -----Answer-----

S = input() # 入力される文字列の長さが4であることを利用する

if len(S) == 4:
    if S[0].isdigit() and S[1].isdigit() and S[2].isdigit() and S[3].isdigit():
        if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
            print("Bad")
        else:
            print("Good")
    else:
        print("Bad")
else:
    print("Bad")

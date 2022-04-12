
S = input()
S_list = list(S)
S_list.sort()

if S_list == ['a', 'b', 'c']:  # 入力された文字がa,b,cのみかどうか判定する
    print("Yes")
else:
    print("No")

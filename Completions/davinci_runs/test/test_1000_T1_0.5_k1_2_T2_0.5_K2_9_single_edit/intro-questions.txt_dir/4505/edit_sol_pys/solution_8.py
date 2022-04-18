

S = input()
S_list = list(S)
S_list.sort()  # sortしてソート済みのリストをS_listに代入

if S_list == ['a', 'b', 'c']:  # ソート済みのリストが['a', 'b', 'c']と一致するか判定
    print("Yes")
else:
    print("No")

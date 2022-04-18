

#-----main-----
a, b, c = input().split() # 3つの入力をスペースで区切り、a,b,cに代入

if (a == "North" and b == "South") or (a == "South" and b == "North") or (a == "East" and b == "West") or (a == "West" and b == "East"): # aとbが逆方向なら
    print("No") # Noを出力
elif (c == "North" and b == "South") or (c == "South" and b == "North") or (c == "East" and b == "West") or (c == "West" and b == "East"): # bとcが逆方向なら
    print("No") # Noを出力
else:
    print("Yes")

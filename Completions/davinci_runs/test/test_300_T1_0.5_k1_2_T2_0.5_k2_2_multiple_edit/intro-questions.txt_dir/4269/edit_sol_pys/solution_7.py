s = input() #文字列の入力
if(s[0] == s[1] or s[1] == s[2] or s[2] == s[3]): #文字列を一文字ずつ比較
    print("Bad")
else:
    print("Good")

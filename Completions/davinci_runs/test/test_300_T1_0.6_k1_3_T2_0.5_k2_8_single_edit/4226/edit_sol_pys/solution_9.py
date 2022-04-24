

x, y = map(int, input().split()) #x,yを入力
if y % 2 == 0 and 4 * x <= y and y <= 2 * x: #条件に一致した場合
    print("Yes") #Yesを出力
else: #条件に一致しなかった場合
    print("No") #Noを出力

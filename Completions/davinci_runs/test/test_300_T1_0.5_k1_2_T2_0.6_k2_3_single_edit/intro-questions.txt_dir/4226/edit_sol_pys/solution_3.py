

# -----Answer-----
x, y = map(int, input().split()) # 入力された文字列を空白で区切り、int型に変換したものをx,yに代入

if y % 2 == 0: # yが偶数の時
    if (x * 2 + 4) / 2 == y: # x*2+4/2=yならYes
        print("Yes")
    else:
        print("No")
else:
    print("No")

# -----Other Answer-----
x, y = map(int, input().split())

if x * 2 <= y <= x * 4:
    if y % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")

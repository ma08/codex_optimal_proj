

x, a, b = map(int, input().split()) #x, a, bを受け取る

if abs(x - a) < abs(x - b): #xとaの距離がxとbの距離より小さいかどうか
    print('A') #小さい場合はAを出力
else:
    print('B')

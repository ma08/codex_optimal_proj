x = int(input().split()[0]) # 座標
n = int(input().split()[0]) # バス停の数
p = [int(i) for i in input().split()] # バス停のリスト
p.sort() # バス停のリストをソート

if x <= p[0]: # 座標が最も近いバス停より左側にあるとき
    print(p[0]-x) # 最も近いバス停までの距離を出力
elif x >= p[-1]: # 座標が最も遠いバス停より右側にあるとき
    print(x-p[-1]) # 最も遠いバス停までの距離を出力
else:
    for i in range(1, n): # 他のバス停について
        if x <= p[i]: # 座標がそのバス停より左側にあるとき
            print(min(x-p[i-1], p[i]-x)) # 座標からそのバス停までの距離の最小値を出力
            break

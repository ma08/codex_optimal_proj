

#-----main-----

a, b = map(int, input().split())  #aとbを入力してint型に変換

if a <= b:   #aがb以下の時
    print(0)   #0を出力
else:
    print(a - b)  #a-bを出力

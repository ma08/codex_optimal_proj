#-----main-----

a, b = map(int, input().split()) #a,bに数値を入力

if a <= b: #aがb以下の場合
    print(0)
else: #aがbより大きい場合
    print(a - b)


s = input() # inputの文字をsに代入
t = input() # inputの文字をtに代入

cnt = 0

for i in range(len(s)): # sの文字数分ループ
    if s[i] == t[0]: # s[i]がt[0]と一致する場合
        cnt += 1
        t = t[1:] # tを1文字減らす
    if len(t) == 0: # tが空になったら
        break

if len(t) == 0: # tが空だったら
    print(len(s) - cnt)
else:
    print(len(s))

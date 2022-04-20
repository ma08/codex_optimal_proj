

n = int(input()) # 入力
h = list(map(int, input().split())) # 入力

for i in range(n-1): # n-1回ループ
    if h[i] > h[i+1]: # h[i]がh[i+1]より大きいなら
        h[i] -= 1 # h[i]を1引く
        if h[i] > h[i+1]: # h[i]がh[i+1]より大きいなら
            print('No') # Noを出力
            exit() # 処理を終了
print('Yes') # Yesを出力

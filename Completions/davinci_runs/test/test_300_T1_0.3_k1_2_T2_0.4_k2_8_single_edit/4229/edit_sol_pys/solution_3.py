

n = int(input()) # 入力

ans = 0 # 初期化

for i in range(1, n+1): # 1からnまで
    if i % 3 == 0 and i % 5 == 0: # 3と5の倍数は除外
        continue
    elif i % 3 == 0: # 3の倍数は除外
        continue
    elif i % 5 == 0: # 5の倍数は除外
        continue
    else: # それ以外
        ans += i

print(ans) # 出力

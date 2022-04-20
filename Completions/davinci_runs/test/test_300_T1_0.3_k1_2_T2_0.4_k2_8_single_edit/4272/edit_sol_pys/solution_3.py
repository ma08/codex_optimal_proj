

N = int(input()) # 整数の入力
S = input() # 文字列の入力

count = 0 # 初期化

for i in range(N-2): # N-2回ループ
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        count += 1 # 加算

print(count) # 出力



N, K = map(int, input().split()) # N,Kをint型に変換したものをlistに格納
D = set(map(int, input().split())) # Dをint型に変換したものをsetに格納

# print(N, K, D) # N,K,Dを標準出力

for i in range(N, 10000): # N~10000までのループ
    if all(d not in str(i) for d in D): # Dの中身がiに含まれていないかどうかを全て満たすなら
        print(i) # iを出力
        break # ループを抜ける

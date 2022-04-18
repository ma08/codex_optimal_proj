

n, k = map(int, input().split()) # n, kを受け取る
t = input() # 文字列を受け取る

ans = "" # 文字列を格納する変数
for i in range(n): # n回繰り返す
    if i < (k - 1) % n: # iがk-1の剰余より小さいとき
        ans += t[i] # ansにt[i]を追加する
    else:
        ans += t[(k - 1) % n] # ansにt[k-1の剰余]を追加する

print(ans)

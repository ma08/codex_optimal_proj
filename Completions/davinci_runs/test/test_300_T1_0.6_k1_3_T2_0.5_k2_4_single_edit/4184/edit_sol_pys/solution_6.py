

N = int(input()) # 入力
W = list(map(int, input().split())) # 複数入力

S1 = 0 # 左側の和
S2 = sum(W) # 右側の和

ans = abs(S1 - S2) # 左側と右側の和の差の絶対値
for i in range(1, N):
    S1 += W[i-1] # 左側の和
    S2 -= W[i-1] # 右側の和
    ans = min(ans, abs(S1 - S2)) # 左側と右側の和の差の絶対値

print(ans)

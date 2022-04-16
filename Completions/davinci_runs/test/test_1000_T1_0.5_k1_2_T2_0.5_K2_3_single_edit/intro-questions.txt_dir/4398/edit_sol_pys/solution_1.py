

N = int(input()) # 入力
S,T = input().split() # 入力

string = "" # 定義
for i in range(N): # 繰り返し
    string += S[i] # 追加
    string += T[i] # 追加
print(string) # 出力

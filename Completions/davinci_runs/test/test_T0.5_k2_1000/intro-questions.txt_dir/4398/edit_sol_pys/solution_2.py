
N = int(input()) # 文字列の長さ
S,T = input().split() # 文字列をスペースで区切って入力

string = "" # 結合した文字列を格納する変数
for i in range(N):
    string += S[i]
    string += T[i]
print(string)

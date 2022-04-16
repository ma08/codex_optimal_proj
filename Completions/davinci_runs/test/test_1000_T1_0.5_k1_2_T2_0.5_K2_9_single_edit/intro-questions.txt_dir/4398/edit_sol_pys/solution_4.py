

N = int(input()) # 文字列の数
S,T = input().split() # 交互に結合したい文字列

string = ""
for i in range(N):
    string += S[i]
    string += T[i]
print(string)

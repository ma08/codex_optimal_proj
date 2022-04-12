

N = int(input())
S,T = input().split()

string = "" # 結合した文字列を格納する変数
for i in range(N):
    string += S[i]
    string += T[i]
print(string)

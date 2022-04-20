# 問題文
# 高橋君は整数を X個持っています。
# これらの整数の内、A以上の整数の個数を求めてください。

X, A = map(int, input().split())
print(max(0,X-A))

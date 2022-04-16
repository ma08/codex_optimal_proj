

n,a,b = map(int,input().split())  # 文字列を数値に変換

if a > b:  # 条件に合った場合の処理
    a,b = b,a  # 値を入れ替える

if a == 0:  # 条件に合った場合の処理
    print(0)
else:
    print(min(n,a))  # min()は引数の中で最小の値を返す

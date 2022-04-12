
N = int(input()) # 入力を整数に変換
X = list(map(int, input().split())) # 入力を整数のリストに変換

def median(l): # 中央値を返す関数
    l.sort() # リストを昇順にソート
    return l[len(l)//2] # リストの中央値を返す

for i in range(N):
    X_copy = X[:] # Xの複製を作成
    X_copy.pop(i) # X_copyからi番目の要素を削除
    print(median(X_copy)) # X_copyの中央値を出力



# 数字のリストを作成
numbers = list(range(1, n + 1))

# 数字のリストを逆順にする
numbers.reverse()

# 結果を出力する
print(*numbers)

n = int(input())
p = list(map(int, input().split()))

# 配列の中で、隣り合う数字が連続しているかを判定する
# 連続していない数字を記憶する
# 連続していない数字が2つ以上あれば、NOを出力する
# そうでなければ、YESを出力する

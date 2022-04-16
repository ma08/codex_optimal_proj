
n = int(input())
a = [0] * 1000000  # 長さ1000000の配列を作成
for i in range(n):
    a[int(input())] += 1  # 入力された値に対応する配列の要素の値をインクリメント
print(sum(map(lambda x: x % 2, a)))  # 奇数の個数を出力



n, l = map(int, input().split())  # 入力を受け取る

flavors = [l + i for i in range(n)]  # リストを生成する

print(sum(flavors) - min([abs(f) for f in flavors]))  # 要素の合計から最小値を引く

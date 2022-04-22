

n, l = map(int, input().split())  # 1行目にn,lを取得

flavors = [l + i for i in range(n)]  # n個のフレーバーを生成

print(sum(flavors) - min([abs(f) for f in flavors]))  # 合計から最も絶対値が小さいものを引く

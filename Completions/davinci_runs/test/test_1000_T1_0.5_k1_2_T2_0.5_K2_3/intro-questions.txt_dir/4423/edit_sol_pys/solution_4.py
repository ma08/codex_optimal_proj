# まずは入力を取り込み、変数nに格納

# 辞書を作る
n = int(input())
# n回ループ
d = {}
    # 入力をタプルに格納
for i in range(n):
    # pを数値に変換
    s, p = input().split()
    # sが辞書のキーに存在しない場合
    p = int(p)
        # そのキーにpをリストとして格納
    if s not in d.keys():
    # sが辞書のキーに存在する場合
        d[s] = [p]
        # そのキーにpをリストとして追加
    else:
        d[s].append(p)
    # それぞれのキーのリストを降順にソート
for s in sorted(d.keys()):
    d[s].sort(reverse=True)
# 辞書のキーをソート
    # それぞれのキーのリストを表示
for s in sorted(d.keys()):
    for p in d[s]:
        print(p)

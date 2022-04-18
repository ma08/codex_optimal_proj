

N, M = map(int, input().split())
count = 0
seats = [0 for i in range(M)]
for i in range(N):  # 入力
    l, r = map(int, input().split())  # 座席の左端と右端を取得
    for j in range(l, r+1):  # 左端から右端までループ
        seats[j-1] += 1  # 座席の空き状況を更新
for i in range(len(seats)):  # 出力
    if seats[i] > 0:  # 座席の空き状況が1以上なら
        count += 1  # 座席の空き数をカウント
print(count)  # カウントした座席の空き数を出力

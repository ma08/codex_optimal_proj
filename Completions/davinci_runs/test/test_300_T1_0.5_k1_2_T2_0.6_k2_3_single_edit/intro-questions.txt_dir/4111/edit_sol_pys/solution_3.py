
n = int(input())  # 数列の長さ
a = list(map(int, input().split()))  # 数列
# 初期化
odds = 0  # 奇数番目の和
evens = 0  # 偶数番目の和
count = 0  # 要素を追加する回数
for i in range(n):  # 奇数番目と偶数番目の和
    if i % 2 == 0:  # 偶数ならば
        evens += a[i]
    else:  # 奇数ならば
        odds += a[i]
for i in range(n):  # 各要素を追加する前に値を更新
    if i % 2 == 0:  # 偶数ならば
        evens -= a[i]
    else:  # 奇数ならば
        odds -= a[i]
    if odds == evens:  # 奇数番目と偶数番目の和が同じならば
        count += 1  # 要素を追加する回数を1増やす
    if i % 2 == 0:  # 偶数ならば
        evens += a[i]
    else:  # 奇数ならば
        odds += a[i]
print(count)  # 答え

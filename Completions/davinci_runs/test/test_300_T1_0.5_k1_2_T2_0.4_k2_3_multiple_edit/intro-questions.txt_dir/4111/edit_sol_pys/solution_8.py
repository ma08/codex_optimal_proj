
n = int(input())  # 入力
a = list(map(int, input().split()))  # 入力

odds = 0  # 奇数番目の合計
evens = 0  # 偶数番目の合計
count = 0  # 答え

for i in range(n):  # 奇数番目の合計と偶数番目の合計を計算
    if i % 2 == 0:  # 偶数番目
        evens += a[i]  # 偶数番目の合計に足す
    else:
        odds += a[i]  # 奇数番目の合計に足す

for i in range(n):  # 奇数番目の合計と偶数番目の合計が等しいものを数える
    if i % 2 == 0:  # 偶数番目
        evens -= a[i]  # 偶数番目の合計から引く
    else:
        odds -= a[i]  # 奇数番目の合計から引く
    if odds == evens:  # 奇数番目の合計と偶数番目の合計が等しいとき
        count += 1  # 答えに1足す
    if i % 2 == 0:  # 偶数番目
        evens += a[i]  # 偶数番目の合計に足す
    else:
        odds += a[i]  # 奇数番目の合計に足す

print(count)  # 答えを出力

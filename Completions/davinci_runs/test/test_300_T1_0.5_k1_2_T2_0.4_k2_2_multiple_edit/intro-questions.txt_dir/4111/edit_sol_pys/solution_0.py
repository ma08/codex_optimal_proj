
n = int(input())  # 入力
a = list(map(int, input().split()))  # 入力

odds = 0  # 奇数の和
evens = 0  # 偶数の和
count = 0  # 合計が等しい数

for i in range(n):  # 偶数と奇数の和を求める
    if i % 2 == 0:  # 偶数
        evens += a[i]  # 偶数の和に加算
    else:
        odds += a[i]  # 奇数の和に加算

for i in range(n):  # 合計が等しい数を求める
    if i % 2 == 0:  # 偶数
        evens -= a[i]  # 偶数の和から引く
    else:
        odds -= a[i]  # 奇数の和から引く
    if odds == evens:  # 合計が等しい場合
        count += 1  # 合計が等しい数に加算
    if i % 2 == 0:  # 偶数
        evens += a[i]  # 偶数の和に加算
    else:
        odds += a[i]  # 奇数の和に加算

print(count)  # 出力



a, b, x = map(int, input().split())  # a:単価, b:桁数, x:残高

if a + b > x:  # 残高が足りない場合は0
    print(0)
    exit()

k = (x - b) // a  # 個数を求める
l = len(str(k))  # 個数の桁数を求める

if a * k + b * l <= x:  # 個数が残高内に収まる場合
    print(k)
else:  # 残高内に収まらない場合は、個数の桁数を1減らす
    print(k - 10 ** (l - 1))

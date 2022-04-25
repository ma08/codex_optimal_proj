
a, b, x = map(int, input().split())  # a:単価 b:桁数 x:残高

if a + b > x:  # 残高が足りない場合
    print(0)
    exit()

k = (x - b) // a  # 個数
l = len(str(k))  # 桁数

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))

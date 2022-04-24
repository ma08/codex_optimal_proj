
a, b, x = map(int, input().split())  # 入力

if a + b > x:  # 0の場合終了
    print(0)
    exit()

k = (x - b) // a  # 値
l = len(str(k))  # 桁数

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))

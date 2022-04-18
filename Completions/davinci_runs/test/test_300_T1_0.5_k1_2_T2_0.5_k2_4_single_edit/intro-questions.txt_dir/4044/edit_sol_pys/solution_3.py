

a, b, x = map(int, input().split())  # 整数の入力

s = "0"*a + "1"*b  # 文字列の初期化

for i in range(a):  # 並び替えの計算
    for j in range(b):
        if i + j == x:
            print(s)
            exit()
        s = s[1:] + s[0]

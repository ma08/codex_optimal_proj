
a, b, x = map(int, input().split()) # 入力

s = "0"*a + "1"*b # 初期化

for i in range(a):
    for j in range(b):
        if i + j == x:
            print(s)
            exit()
        s = s[1:] + s[0]


a, b, x = map(int, input().split())

s = "0"*a + "1"*b # 0と1を組み合わせた文字列を作成

for i in range(a):
    for j in range(b):
        if i + j == x:
            print(s)
            exit()
        s = s[1:] + s[0] # 先頭の文字を末尾に移動

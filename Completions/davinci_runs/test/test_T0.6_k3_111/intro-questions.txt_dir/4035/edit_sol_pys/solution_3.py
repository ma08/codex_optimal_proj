
a, b = map(float, input().split())

for i in range(1, 101):
    if (i * 0.08) == a and (i * 0.1) == b:  # 小数点以下の桁数を指定しないと正しく判定できない
        print(i)
        exit()

print(-1)

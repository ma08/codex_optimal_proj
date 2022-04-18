

a, b, c = map(int, input().split())  # a, b, c に整数を入力する

print(min(a + b, a + c, b + c))  # 足した数字を全て比較する

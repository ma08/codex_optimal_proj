

x, n = map(int, input().split())  # 入力
p = set(map(int, input().split()))  # 入力

for i in range(0, 200):  # 計算
    if x - i not in p:  # 計算
        print(x - i)  # 出力
        exit()
    elif x + i not in p:  # 計算
        print(x + i)  # 出力
        exit()

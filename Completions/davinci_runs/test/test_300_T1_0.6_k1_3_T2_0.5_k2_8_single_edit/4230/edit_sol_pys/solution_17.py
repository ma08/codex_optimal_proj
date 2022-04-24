

x, _ = map(int, input().split())
p = set(map(int, input().split()))  # 初期化してから値を入れる

for i in range(0, 200):
    if x - i not in p:
        print(x - i)
        exit()
    elif x + i not in p:
        print(x + i)
        exit()

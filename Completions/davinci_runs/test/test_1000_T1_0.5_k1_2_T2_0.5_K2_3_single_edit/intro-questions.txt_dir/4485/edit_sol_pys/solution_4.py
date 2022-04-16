
n, m = map(int, input().split())

# 各島に繋がる島を辞書に格納する
island_dict = {}
for i in range(1, n+1):
    island_dict[i] = []

# 島に繋がる島を辞書に格納する
for _ in range(m):
    a, b = map(int, input().split())
    island_dict[a].append(b)
    island_dict[b].append(a)

# 島1から繋がる島を探す
island_1_list = island_dict[1]
# 島1から繋がる島から、島Nに繋がる島があればPOSSIBLE、なければIMPOSSIBLEを出力する
for i in island_1_list:
    if n in island_dict[i]:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')

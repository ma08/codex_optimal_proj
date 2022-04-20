

N, M = map(int, input().split())

year_to_prefecture = {}
for i in range(M):
    P, Y = map(int, input().split())
    if Y in year_to_prefecture:
        year_to_prefecture[Y].append(P)
    else:
        year_to_prefecture[Y] = [P]

year_list = sorted(list(year_to_prefecture.keys()))

prefecture_to_city_num = {}
for year in year_list:
    for prefecture in year_to_prefecture[year]:
        if prefecture in prefecture_to_city_num:
            prefecture_to_city_num[prefecture] += 1
        else:
            prefecture_to_city_num[prefecture] = 1

for year in year_list:
    for prefecture in year_to_prefecture[year]:
        print(str(prefecture).zfill(6) + str(prefecture_to_city_num[prefecture]).zfill(6))
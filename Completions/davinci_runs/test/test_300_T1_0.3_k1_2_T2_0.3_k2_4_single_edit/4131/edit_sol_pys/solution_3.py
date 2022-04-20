

N, M = map(int, input().split())
P_Y = [list(map(int, input().split())) for _ in range(M)]
#N, M = 2, 3
#P_Y = [[1, 32], [2, 63], [1, 12]]

print(N, M)
print(P_Y)

# 各県の都市数
city_num_per_pref = [0] * N
for p, y in P_Y:
    city_num_per_pref[p-1] += 1

print(city_num_per_pref)

# 各県の都市のID
id_per_pref = [[0] * c for c in city_num_per_pref]
for p, y in P_Y:
    id_per_pref[p-1][city_num_per_pref[p-1]-1] = y
    city_num_per_pref[p-1] -= 1

#print(id_per_pref)

# 各県の都市のIDをソート
for pref in id_per_pref:
    pref.sort()

#print(id_per_pref)

# 各県の都市のIDをIDに変換
id_per_pref = [[str(p).zfill(6) + str(i+1).zfill(6) for i in range(len(pref))] for p, pref in enumerate(id_per_pref, 1)]

#print(id_per_pref)

# 各県の都市のIDを結合
id_per_pref = [id for pref in id_per_pref for id in pref]

#print(id_per_pref)

# 出力
for id in id_per_pref:
    print(id)

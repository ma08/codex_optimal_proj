
# 解答
# N: グループ数
# l_i: i 番目のグループの座席の左端
# r_i: i 番目のグループの座席の右端

N = int(input())

# 座席を表すリストを作成
# 座席の人数を表す（0は空席、1は1人が座っている）
seats = [0] * 100000

for i in range(N):
    l_i, r_i = map(int, input().split())
    for j in range(l_i - 1, r_i):  # 座席番号は 1 から始まるが、リストは 0 から始まるので -1 しておく
        seats[j] = 1

print(sum(seats))

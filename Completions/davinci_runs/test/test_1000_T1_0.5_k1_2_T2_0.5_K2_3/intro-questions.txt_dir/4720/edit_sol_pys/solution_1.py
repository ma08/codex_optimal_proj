# https://atcoder.jp/contests/abc066/tasks/abc066_a

# 解答
# N: グループ数
# L_i: i番目のグループの座席の左端
# R_i: i番目のグループの座席の右端

N = int(input())

# 座席を表すリストを作成
# 座席の人数を表す（0は空席、1は1人が座っている）
seats = [0] * 100000

for i in range(N):
    L_i, R_i = map(int, input().split())
    for j in range(L_i - 1, R_i):  # 座席番号は1から始まるが、リストは0から始まるので-1しておく
        seats[j] = 1

print(sum(seats))

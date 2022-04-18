

# 解答例
# N: 座席数
# M: 人数

M = int(input())
N = int(input())

# 座席を表すリストを作成（0は空席、1は1人が座っている）
seats = [0] * N

for _ in range(M):
    a = int(input())
    seats[a - 1] = 1

print(sum(seats))

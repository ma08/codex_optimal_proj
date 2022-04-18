
# 標準入力から数字を取得する

# 標準入力から数字を取得し、リストに格納する
N = int(input())
a = list(map(int, input().split()))

# 方針: 平均を取る
# a_iをすべて同じ数にするのは、a_iを平均にするのと同じ
# したがって、平均を取って、それらとの差を計算していく

# 平均の取り方
# sum()で合計を取る
# len()で要素数を取る
# 両者を割る

# 平均を取る
average = sum(a) / len(a)

# 平均との差を計算
# 平均との差を計算し、２乗したものを足していく
diff_total = 0
for i in range(N):
    diff_total += (a[i] - average) ** 2

print(int(diff_total))

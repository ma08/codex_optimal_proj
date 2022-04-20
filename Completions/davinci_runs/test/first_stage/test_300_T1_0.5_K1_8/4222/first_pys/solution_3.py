

# 初期化
num_snukes = int(input())
num_snacks = int(input())
snack_list = []
for i in range(num_snacks):
    snack_list.append(list(map(int, input().split())))

# 全スナックを持つスナックにチェックをつける
snack_check = [0] * num_snukes
for snack in snack_list:
    for i in range(1, len(snack)):
        snack_check[snack[i] - 1] += 1

# スナックを持たないスナックをカウント
count = 0
for i in range(num_snukes):
    if snack_check[i] == 0:
        count += 1

print(count)
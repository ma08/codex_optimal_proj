

n = int(input())  # 入力
p = list(map(int, input().split()))  # 入力

count = 0  # 初期化

for i in range(1, n - 1):
    if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
        count += 1
print(count)  # 出力

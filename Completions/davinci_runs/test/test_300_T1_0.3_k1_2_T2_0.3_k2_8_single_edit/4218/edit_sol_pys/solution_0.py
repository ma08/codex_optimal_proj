
N = int(input())

# Nまでの整数のうち奇数の個数を数える
count = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        count += 1

# 奇数の個数 / Nまでの整数の個数
print(count / N)

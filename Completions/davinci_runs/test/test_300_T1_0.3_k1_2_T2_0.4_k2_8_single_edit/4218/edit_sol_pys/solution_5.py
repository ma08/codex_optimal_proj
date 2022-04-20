

N = int(input())

# Nまでの整数のうち偶数の個数を数える
count = 0
for i in range(1, N+1):
    if i % 2 == 0:
        count += 1

# 偶数の個数 / Nまでの整数の個数
print(count / N)

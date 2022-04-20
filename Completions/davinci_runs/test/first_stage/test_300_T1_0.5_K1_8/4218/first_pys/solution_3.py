

# My Answer
N = int(input())

# 全体の合計
total = 0
for i in range(1, N+1):
    total += i

# 奇数の合計
odd = 0
for i in range(1, N+1):
    if i % 2 == 1:
        odd += i

print(odd / total)

# Answer
N = int(input())

# 全体の合計
total = 0
for i in range(1, N+1):
    total += i

# 奇数の合計
odd = 0
for i in range(1, N+1):
    if i % 2 == 1:
        odd += i

print(odd / total)
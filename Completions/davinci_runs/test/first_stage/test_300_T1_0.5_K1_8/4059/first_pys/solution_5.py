

import sys

N = int(sys.stdin.readline())

# エラトステネスの篩
prime_list = [0] * (N + 1)
for i in range(2, N + 1):
    if prime_list[i] == 0:
        for j in range(2 * i, N + 1, i):
            prime_list[j] = 1

# 合成数のリスト
composite_list = []
for i in range(2, N + 1):
    if prime_list[i] == 1:
        composite_list.append(i)

count = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i * j + 1 > N:
            break
        elif prime_list[i * j + 1] == 0:
            count += 1

print(count)
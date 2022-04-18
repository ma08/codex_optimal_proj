
N = int(input())

odd_count = 0
for i in range(1, N + 1):
    if len(str(i)) % 2 == 1:  # 偶数の場合は、0になる
        odd_count += 1

print(odd_count)


N = int(input())

odd_count = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        odd_count += 1

print(odd_count / N)

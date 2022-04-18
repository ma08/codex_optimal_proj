
N, K = map(int, input().split())

count = 0
for i in range(1, N + 1):
    if i % K == 0:
        count += 1
print(count)

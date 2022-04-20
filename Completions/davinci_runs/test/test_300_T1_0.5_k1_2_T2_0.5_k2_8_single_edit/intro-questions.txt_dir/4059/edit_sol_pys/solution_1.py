
N = int(input())

ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        k = N - i*j
        if k > 0:
            ans += 1

print(count)

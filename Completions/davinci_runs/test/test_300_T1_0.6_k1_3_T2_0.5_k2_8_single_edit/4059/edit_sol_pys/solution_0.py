

N = int(input())

ans = 0

for a in range(1, N):
    b = (N - a) // 2
    if 2 * a + 2 * b == N:
        ans += 3
    if 2 * a + 2 * b + 1 == N:
        ans += 4

print(ans)

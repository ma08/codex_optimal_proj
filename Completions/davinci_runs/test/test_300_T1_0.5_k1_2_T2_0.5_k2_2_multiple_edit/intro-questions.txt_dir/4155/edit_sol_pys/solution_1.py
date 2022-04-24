
n = int(input())  # 数列の長さ
h = list(map(int, input().split()))  # 数列

ans = 0
for i in range(n):
    if h[i] > 0:
        ans += 1
        for j in range(i+1, n):
            if h[j] > 0:
                h[j] -= 1

print(ans)

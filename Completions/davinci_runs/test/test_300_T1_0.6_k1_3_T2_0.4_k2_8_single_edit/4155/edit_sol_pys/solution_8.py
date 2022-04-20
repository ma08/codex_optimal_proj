

N = int(input())
h = list(map(int, input().split()))  # 入力をリストにする

ans = 0
for i in range(N):
    ans += abs(h[i] - (i + 1))  # h[i]とi+1の差の絶対値を足す

print(ans)

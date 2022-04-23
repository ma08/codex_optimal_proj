

N, A, B = map(int, input().split())
h = [int(input()) for i in range(N)]

ans = 0  # 必要な回数
for i in range(N):
    # 必要な攻撃回数
    cnt = max(0, h[i] - B * A)
    ans += cnt // (A - B)
    if cnt % (A - B) != 0:
        ans += 1

print(ans)

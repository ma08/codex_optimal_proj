

# TODO
# https://atcoder.jp/contests/abc117/tasks/abc117_d

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(40, -1, -1):
    # i桁目の1の個数
    cnt = 0
    for a in A:
        if (a >> i) & 1:
            cnt += 1
    if cnt < N/2:
        # i桁目が0になる方がいい
        ans += (N - cnt) * (1 << i)
    else:
        # i桁目が1になる方がいい
        ans += cnt * (1 << i)
        # i桁目が1となる個数のAを作る
        B = []
        for a in A:
            if (a >> i) & 1:
                B.append(a)
        A = B
print(ans)

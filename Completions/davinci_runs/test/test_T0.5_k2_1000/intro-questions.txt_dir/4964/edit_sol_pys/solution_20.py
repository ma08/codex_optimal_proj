

# Solution
def solve():
    N, H, L = map(int, input().split())
    horror_list = list(map(int, input().split()))
    similarities = [list(map(int, input().split())) for _ in range(L)]
    HI = [0] * (N + 1)  # HI[i] = i番目の映画がホラー映画かどうか
    for i in range(N):
        if i + 1 in horror_list:
            HI[i + 1] = 0
        else:
            HI[i + 1] = float('inf')  # ホラー映画でない
    for a, b in similarities:
            HI[b] = HI[a] + 1  # aがホラー映画でないならばbもホラー映画でない
        elif HI[b] + 1 < HI[a]:  # bがホラー映画でないならばaもホラー映画でない
            HI[a] = HI[b] + 1
    print(HI.index(max(HI)))

solve()

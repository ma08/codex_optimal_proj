
# Solution
def solve():
    N, H, L = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similarities = [list(map(int, input().split())) for _ in range(L)] # 同じ部屋にいる人のリスト

    HI = [0] * N
    for i in range(N):
        if i in horror_list: # 怖い人は0
            HI[i] = 0
        else:
            HI[i] = float('inf') # 怖い人以外はinf

    for a, b in similarities:
        if HI[a] < HI[b]:
            HI[b] = HI[a] + 1
        elif HI[b] < HI[a]:
            HI[a] = HI[b] + 1
    print(HI.index(max(HI)))

solve()

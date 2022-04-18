
# Solution
def solve():
    n, h, l = map(int, input().split())
    horror_list = set(map(int, input().split())) # ホラー映画リスト
    similarities = [list(map(int, input().split())) for _ in range(l)] # 類似度リスト
    hi = [0] * n # ホラー映画度
    for i in range(n):
        if i in horror_list: # ホラー映画度が0
            hi[i] = 0
        else: # ホラー映画度がinf
            hi[i] = float('inf')
    for a, b in similarities: # 類似度リストをループ
        if hi[a] < hi[b]:
            hi[b] = hi[a] + 1
        elif hi[b] < hi[a]:
            hi[a] = hi[b] + 1
    print(hi.index(max(hi)))

solve()

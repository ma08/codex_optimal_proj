# https://atcoder.jp/contests/abc079/tasks/abc079_c

# Solution
def solve():
    N, H, L = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similar_list = [list(map(int, input().split())) for _ in range(L)]
    HI = [0] * N
    for i in range(N):
        if i in horror_list:
            HI[i] = 0
        else:
            HI[i] = float('inf')
    for a, b in similar_list:
        if HI[a] < HI[b]:
            HI[b] = HI[a] + 1
        elif HI[b] < HI[a]:
            HI[a] = HI[b] + 1
    print(HI.index(max(HI)))

solve()

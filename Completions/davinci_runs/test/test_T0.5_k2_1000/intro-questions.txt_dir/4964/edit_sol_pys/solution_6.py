

# Solution
def solve():
    N, H, L = map(int, input().split())
    horror_list = list(map(int, input().split()))
    similarities = [list(map(int, input().split())) for _ in range(L)]
    HI = [float('inf')] * (N + 1)
    for i in range(N):
        if i + 1 in horror_list:
            HI[i + 1] = 0 
    for a, b in similarities:
        if HI[a] + 1 < HI[b]:
            HI[b] = HI[a] + 1 
        elif HI[b] + 1 < HI[a]:
            HI[a] = HI[b] + 1 
    print(HI.index(max(HI)))

solve()

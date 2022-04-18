

# Solution
def solve():
    N, H, L = map(int, input().split()) # number of books, number of horror books, number of similarities
    horror_list = set(map(int, input().split())) # list of horror books
    similarities = [list(map(int, input().split())) for _ in range(L)]
    HI = [0] * N # list of horror index
    for i in range(N):
        if i in horror_list:
            HI[i] = 0
        else:
            HI[i] = float('inf')
    for a, b in similarities:
        if HI[a] < HI[b]:
            HI[b] = HI[a] + 1
        elif HI[b] < HI[a]:
            HI[a] = HI[b] + 1
    print(HI.index(max(HI)))

solve()

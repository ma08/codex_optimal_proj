
# Solution
def solve():
    n, h, l = map(int, input().split())
    horrors = set(map(int, input().split()))
    similar_movies = [list(map(int, input().split())) for _ in range(l)]
    hi = [0] * n
    for i in range(n):
        hi[i] = 0 if i in horrors else float('inf')
    for a, b in similar_movies:
        if hi[a] < hi[b]:
            hi[b] = hi[a] + 1
        elif hi[b] < hi[a]:
            hi[a] = hi[b] + 1
    print(hi.index(max(hi)))


solve()

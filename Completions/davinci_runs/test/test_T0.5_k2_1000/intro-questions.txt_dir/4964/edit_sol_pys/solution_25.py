

# solution:

N, H, L = map(int, input().split())
horror = set(map(int, input().split()))  # set of horror movies

similar = {}  # similar[i] = set of similar movies to i
for _ in range(L):
    a, b = map(int, input().split())
    similar[a] = similar.get(a, set()).union({b})
    similar[b] = similar.get(b, set()).union({a})

HI = [0] * N  # HI[i] = number of horror movies in the longest chain of similar movies that ends with movie i
for h in horror:
    HI[h] = 0

Q = 0
while Q < N:
    Q = max(HI) + 1
    for i in range(N):
        if HI[i] == 0:
            continue
        else:
            HI[i] = Q if all(HI[j] == 0 for j in similar.get(i, [])) else float('inf')

print(HI.index(max(HI)))

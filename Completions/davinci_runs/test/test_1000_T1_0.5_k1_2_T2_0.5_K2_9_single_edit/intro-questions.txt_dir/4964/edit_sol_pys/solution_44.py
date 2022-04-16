
#Solution:

N, H, L = map(int, input().split())
horror = list(map(int, input().split()))

similar = {}
for _ in range(L):
    a, b = map(int, input().split())
    similar[a] = similar.get(a, set()).union({b}) | {a}
    similar[b] = similar.get(b, set()).union({a}) | {b}

HI = [0] * N  # horror index
for h in horror:  # set horror index of horror movies to 0
    HI[h] = 0  # 0 means not horror

Q = 0  # number of horror movies
while Q < N:  # until all movies are horror
    Q = max(HI) + 1  # increase horror index
    for i in range(N):  # for all movies
        if HI[i] == 0:  # if not horror
            continue  # skip
        else:  # if horror
            HI[i] = Q if all(HI[j] == 0 for j in similar.get(i, [])) else float('inf')  # if all similar movies are not horror, then it is horror, otherwise it is not horror

print(HI.index(max(HI)))

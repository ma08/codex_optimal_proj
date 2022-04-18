
# I think this is a good example of how to use bit operations

N, M = [int(n) for n in input().split()]

like_foods = [0] * N
for i in range(N):
    like_foods[i] = 0
    _, *foods = [int(n) for n in input().split()]
    for food in foods:
        like_foods[i] |= (1 << (food - 1))

count = 0
for i in range(M):
    like_count = 0
    for j in range(N):
        if like_foods[j] & (1 << i) > 0:
            like_count += 1
    if like_count == N:
        count += 1

print(count)

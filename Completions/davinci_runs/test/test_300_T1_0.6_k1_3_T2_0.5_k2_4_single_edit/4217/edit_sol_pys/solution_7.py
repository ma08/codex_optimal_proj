

# I think this is a good example of how to use bit operations.

N, M = [int(n) for n in input().split()]

like_foods = [0] * (N + 1)
for i in range(1, N + 1):
    like_foods[i] = 0  # initialize
    _, *foods = [int(n) for n in input().split()]  # read and split
    for food in foods:
        like_foods[i] |= (1 << (food - 1))  # set bits

count = 0
for i in range(1, M + 1):
    like_count = 0
    for j in range(1, N + 1):
        if like_foods[j] & (1 << (i - 1)) > 0:
            like_count += 1
    if like_count == N:  # all N people like this food
        count += 1

print(count)

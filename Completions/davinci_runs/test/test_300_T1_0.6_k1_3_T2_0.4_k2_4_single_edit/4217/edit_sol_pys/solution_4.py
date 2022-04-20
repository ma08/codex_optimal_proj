

# I think this is a good example of how to use bit operations.
# I'm not sure if this is the best way to do it though.

N, M = [int(n) for n in input().split()]

likes = [0] * N
for i in range(N):  # O(N)
    likes[i] = 0
    _, *foods = [int(n) for n in input().split()]
    for food in foods:
        likes[i] |= (1 << (food - 1))

# Now it's just a simple loop.
count = 0
for i in range(1, M + 1):  # O(M)
    like_count = 0
    for j in range(N):  # O(N)
        if likes[j] & (1 << (i - 1)) > 0:
            like_count += 1
    if like_count == N:
        count += 1

print(count)

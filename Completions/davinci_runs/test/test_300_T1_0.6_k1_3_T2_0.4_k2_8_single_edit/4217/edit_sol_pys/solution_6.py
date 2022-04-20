
# I think this is a good example of how to use bit operations

N, M = [int(n) for n in input().split()]

like_foods = [0] * N  # this is a list of bitmaps
for i in range(N):  # loop through the list of people
    like_foods[i] = 0  # initialize the bitmap
    _, *foods = [int(n) for n in input().split()]  # get the foods
    for food in foods:  # loop through the foods
        like_foods[i] |= (1 << (food - 1))  # set the bit

# Now it's just a simple loop
count = 0
for i in range(1, M + 1):
    like_count = 0
    for j in range(N):
        if like_foods[j] & (1 << (i - 1)) > 0:
            like_count += 1
    if like_count == N:
        count += 1

print(count)

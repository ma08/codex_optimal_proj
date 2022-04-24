

# I think this is a good example of how to use bit operations.
# The idea is to set each bit of an integer to represent a food.
# Each person has a binary number that specifies which food he likes.
# The function of bitwise OR is to get a binary number that represents
# all the foods that one person likes.
# Then the function of bitwise AND is to check if a food is liked by all people.

N, M = [int(n) for n in input().split()]

like_foods = [0] * N
for i in range(N):
    like_foods[i] = 0
    _, *foods = [int(n) for n in input().split()]
    for food in foods:
        like_foods[i] |= (1 << (food - 1))

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

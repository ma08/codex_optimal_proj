
#
# https://www.hackerrank.com/challenges/restaurant/problem
#

#
# I think this is a good example of how to use bit operations.
# After reading the input, we create a list of integers, where each integer
# represents a person, and each bit of the integer represents a food.
#
# Then we loop through the list and count the number of people who like each
# food.
#

import sys

N, M = [int(n) for n in sys.stdin.readline().split()]

like_foods = [0] * N
for i in range(N):
    like_foods[i] = 0
    _, *foods = [int(n) for n in sys.stdin.readline().split()]
    for food in foods:
        like_foods[i] |= (1 << (food - 1))

count = 0
    # Now it's just a simple loop
    like_count = 0
    for j in range(N):
        if like_foods[j] & (1 << (i - 1)) > 0:
            like_count += 1
    if like_count == N:
        count += 1

print(count)

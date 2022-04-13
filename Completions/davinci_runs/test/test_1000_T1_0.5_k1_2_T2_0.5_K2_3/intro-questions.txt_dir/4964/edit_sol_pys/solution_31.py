
# Question:
# Given a list of N horror movies, each with a horror index.
# Given a list of L pairs of similar movies.
# Find which movie is the most scary.
#
# Input Format:
# Each line of input contains the following:
#   N H L - Number of movies, horror index of the most scary movie and the number of similar pairs.
#   horror - List of horror indices of movies.
#   a b - Similar movies.
#
# Output Format:
# Print the index of the movie which is the most scary.
#
# Sample Input:
# 5 2 4
# 1 2 3 4 5
# 1 2
# 2 3
# 3 4
# 4 5
#
# Sample Output:
# 2
#
# Explanation:
# The most scary movie is movie 2.

# Solution:

N, H, L = map(int, input().split())
horror = set(map(int, input().split()))

similar = {}
for _ in range(L):
    a, b = map(int, input().split())
    similar[a] = similar.get(a, set()).union({b})
    similar[b] = similar.get(b, set()).union({a})

HI = [0] * N
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


"""
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


n = int(input())
d = list(map(int, input().split()))

lineup = [0] * n

for i in range(1, n):
    lineup[d[i-1]] = i

print(*lineup)



# A simple problem of combinatorics.

from itertools import permutations

n = int(input())   # number of students

s = list(map(int, input().split()))   # number of books each student owns

for order in permutations(range(1, n+1)):
    books = 0
    for i in order:  # for each student in the order
        books += s[i-1]
        if books > sum(s):
            break
    else:
        print(" ".join(map(str, order)))
        break

print("impossible")

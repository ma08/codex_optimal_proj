
from itertools import combinations_with_replacement

b, d, c, l = map(int, input().split())

solutions = [
    (i, j, k)
    for i, j, k in combinations_with_replacement(range(l // b + 1), 3)
    if i * b + j * d + k * c == l
]

if len(solutions) == 0:
    print("impossible")
else:
    for solution in sorted(solutions):
        print(" ".join([str(x) for x in solution]))

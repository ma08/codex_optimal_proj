b, d, c, l = [int(x) for x in input().split()]
solutions = []

for i in range(l // b + 1):
    for j in range(l // d + 1):
        for k in range(l // c + 1):
            if i * b + j * d + k * c == l:
                solutions.append((i, j, k))
if len(solutions) == 0:
    print("impossible")
else:
    for solution in sorted(solutions):
        print(" ".join([str(x) for x in solution]))

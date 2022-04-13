
a, b, c, d = [int(x) for x in input().split()]

solutions = []

for i in range(d // a + 1):
    for j in range(d // b + 1):
        for k in range(d // c + 1):
            if i * a + j * b + k * c <= d:
                solutions.append((i, j, k))

if len(solutions) == 0:
    print("impossible")
else:
    for solution in sorted(solutions):
        print(" ".join([str(x) for x in solution]))

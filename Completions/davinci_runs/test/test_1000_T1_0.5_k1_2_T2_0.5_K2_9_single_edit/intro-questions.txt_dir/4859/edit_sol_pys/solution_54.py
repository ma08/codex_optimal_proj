

b, d, c, l = map(int, input().split())

solutions = set()

for i in range(l // b + 1):
    for j in range(l // d + 1):
        for k in range(l // c + 1):
            if i * b + j * d + k * c == l:
                solutions.add((i, j, k))

if len(solutions) == 0:
    print("impossible")
else:
    for solution in solutions:
        print(" ".join([str(x) for x in solution]))

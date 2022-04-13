

b, d, c, length = [int(x) for x in input().split()]
print(length)
solutions = []

for i in range(length // b + 1):
    for j in range(length // d + 1):
        for k in range(length // c + 1):
            if i * b + j * d + k * c == length:
                solutions.append((i, j, k))

if len(solutions) == 0:
    print("impossible")
else:
    for solution in sorted(solutions):
        print(" ".join([str(x) for x in solution]))

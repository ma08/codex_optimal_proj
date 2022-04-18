

a, b, c, l = [int(x) for x in input().split()]

solutions = []

for i in range(l // b + 1): # for a in range(l // a + 1):
    for j in range(l // d + 1): # for b in range(l // b + 1):
        for k in range(l // c + 1): # for c in range(l // c + 1):
            if i * b + j * d + k * c == l: # if a * a + b * b + c * c == l:
                solutions.append((i, j, k)) # solutions.append((a, b, c))

if len(solutions) == 0:
    print("impossible")
else:
    for solution in sorted(solutions):
        print(" ".join([str(x) for x in solution]))


b, d, c, l = map(int, input().split())

solutions = []
for i in range(l//b + 1):
    for j in range(l//d + 1):
        for k in range(l//c + 1):
            if i * b + j * d + k * c == l:
                solutions.append([i, j, k])

if len(solutions) == 0:
    print("impossible")
else:
    for i in sorted(solutions):
        print(i[0], i[1], i[2])

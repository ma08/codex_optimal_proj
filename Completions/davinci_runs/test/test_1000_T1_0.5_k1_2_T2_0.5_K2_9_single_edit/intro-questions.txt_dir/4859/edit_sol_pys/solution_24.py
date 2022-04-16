

# This solution is incredibly slow, but it works. It uses brute force to find all possible combinations.


def solve(b, d, c, l, solutions):
    if b + d + c > l:
        return
    if b + d + c == l and [b, d, c] not in solutions:
        solutions.append([b, d, c])
    for i in range(l // b + 1):
        for j in range(l // d + 1):
            for k in range(l // c + 1):
                if i * b + j * d + k * c == l:
                    solutions.append([i, j, k])

b, d, c, l = map(int, input().split())
solve(b, d, c, l, solutions)
solve(b, c, d, l, solutions)
solve(c, b, d, l, solutions)
solve(c, d, b, l, solutions)
solve(d, b, c, l, solutions)
solve(d, c, b, l, solutions)

if len(solutions) == 0:
    print("impossible")
else:
    for i in sorted(solutions):
        print(i[0], i[1], i[2])





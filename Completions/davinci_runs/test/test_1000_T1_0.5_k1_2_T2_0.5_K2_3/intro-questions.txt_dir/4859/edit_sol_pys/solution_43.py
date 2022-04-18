

# This solution is incredibly slow, but it works. It uses brute force to find all possible combinations

b, d, c, l = map(int, input().split())

def solve(b, d, c, l):
    if b + d + c > l:
        return None
    if b + d + c == l:
        return [b, d, c]
    for i in range(l//b + 1):
        for j in range(l//d + 1):
            for k in range(l//c + 1):
                if i * b + j * d + k * c == l:
                    return [i, j, k]
    return None

solutions = []
for i in range(l // b + 1):
    for j in range(l // d + 1):
        for k in range(l // c + 1):
            if i * b + j * d + k * c == l and i * b + j * d + k * c > 0:
                solutions.append((i, j, k))

if len(solutions) == 0:
    print("impossible")
else:
    for i in sorted(solutions, key=lambda x: (x[0] + x[1] + x[2], x[0] * b, x[1] * d, x[2] * c)):
        print(i[0], i[1], i[2], sep=' ')

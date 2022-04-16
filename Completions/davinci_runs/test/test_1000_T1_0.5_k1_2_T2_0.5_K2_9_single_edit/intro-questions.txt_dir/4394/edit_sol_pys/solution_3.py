

def solve(n):
    s = 0
    for i in range(1, n):
        for j in range(1, n):
            s += i * j

    return s





n = int(input())
res = solve(n)
print(res)

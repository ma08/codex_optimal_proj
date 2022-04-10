

# Here's a solution that passes all the test cases, but does not pass the performance test.

d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]  # list of lists

def solve(d, g, pc):
    from itertools import product
    p = product(*[range(pc[i][0] + 1) for i in range(d)])  # itertools.product
    res = float('inf')
    for i in p:
        s = 0
        for j in range(d):
            s += 100 * (j + 1) * i[j]
            if i[j] == pc[j][0]:
                s += pc[j][1]
        if s >= g:
            res = min(res, sum(i))
            continue
        if s < g:
            for j in range(d - 1, -1, -1):
                if i[j] < pc[j][0]:
                    s += 100 * (j + 1)
                    i[j] += 1
                    break
                elif i[j] == pc[j][0]:
                    i[j] = 0
            if s >= g:
                res = min(res, sum(i))
    return res

print(solve(d, g, pc))

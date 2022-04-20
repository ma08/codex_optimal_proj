

d, g = map(int, input().split())

problem = []

for i in range(d):
    p, c = map(int, input().split())
    problem.append([p, c])

problem = sorted(problem, key=lambda x: -x[0])

ans = 0

for i in range(d):
    p, c = problem[i]
    if (g - c) // (100 * (i + 1)) < p:
        ans += (g - c) // (100 * (i + 1))
        g -= (g - c) // (100 * (i + 1)) * (100 * (i + 1))
    else:
        ans += p
        g -= p * (100 * (i + 1)) + c

print(ans)
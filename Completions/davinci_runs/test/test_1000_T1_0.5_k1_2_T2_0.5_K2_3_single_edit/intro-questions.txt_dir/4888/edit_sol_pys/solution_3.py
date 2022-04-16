
n, T = map(int, input().split())
tasks = map(int, input().split())

t = 0
i = 0
while t < T and i < n:
    t += tasks[i]
    i += 1

print(i)

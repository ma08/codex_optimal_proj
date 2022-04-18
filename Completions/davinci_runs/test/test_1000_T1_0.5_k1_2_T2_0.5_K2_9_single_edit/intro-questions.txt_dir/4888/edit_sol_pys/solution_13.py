
n, T = map(int, input().split())
tasks = list(map(int, input().split()))

t = 0
i = 1
while t + tasks[i] <= T and i < n:
    t += tasks[i]
    i += 1

while t + tasks[0] <= T and i < n:
    t += tasks[i]
    i += 1

print(i)

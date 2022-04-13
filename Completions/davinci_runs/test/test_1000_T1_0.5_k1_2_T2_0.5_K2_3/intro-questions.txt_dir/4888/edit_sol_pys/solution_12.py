
n, T = map(int, input().split())
tasks = list(map(int, input().split()))

time = 0
i = 0
while time < T and i < n:
    time += tasks[i]
    i += 1

print(i)

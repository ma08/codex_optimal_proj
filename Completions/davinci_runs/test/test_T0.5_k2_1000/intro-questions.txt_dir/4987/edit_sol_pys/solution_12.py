
n, c, k = map(int, input().split())
d = list(map(int, input().split()))

d.sort()

machines = 0
machine_load = 0

for i in range(n):
    if machine_load >= c or (machine_load > 0 and d[i] - d[i - 1] > k):
        machine_load = 0
        machines += 1
    machine_load += 1

if machine_load > 0:
    machines += 1

print(machines)

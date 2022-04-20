

n = int(input().split()[0])
d = int(input().split()[1])

num_inspectors = 0
start = 1
while start <= n:
    num_inspectors += 1
    start += 2 * d + 1

print(num_inspectors)

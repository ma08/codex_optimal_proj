n = int(input())
days = [int(x) for x in input().split()]

cleanup = 1
dirtiness = days[0]

for day in days[1:]:
    if dirtiness >= 20:
        cleanup += 1
        dirtiness = 0

print(cleanup)

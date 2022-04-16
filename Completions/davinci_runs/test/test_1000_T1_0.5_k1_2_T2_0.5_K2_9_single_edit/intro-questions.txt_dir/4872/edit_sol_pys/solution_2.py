
n = int(input())
days = [int(x) for x in input().split()]

cleanups = 0
dirtiness_level = 0

for day in days:
    dirtiness_level += day
    if dirtiness_level >= 20:
        cleanups += 1
        dirtiness_level = 0

print(cleanups)


n = int(input())
days = [int(x) for x in input().split()]
cleanups = 0
dirtiness = 0

for day in days:
    dirtiness += day
    if dirtiness >= n:
        cleanups += 1
        dirtiness = 0

print(cleanups)

n = int(input()) # number of days
pushes = [int(input()) for _ in range(n)] # read all the pushes

cleanups = 0 # number of cleanups
dirtiness = 0 # number of dirty days

for day in range(1, 367):
    dirtiness += sum([max(0, day - push) for push in pushes if push <= day])
    if dirtiness >= 20:
        cleanups += 1
        dirtiness = 0

print(cleanups)

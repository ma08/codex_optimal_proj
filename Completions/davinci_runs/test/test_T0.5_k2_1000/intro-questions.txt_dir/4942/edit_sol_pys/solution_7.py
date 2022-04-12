

# TODO: fix algorithm - it doesn't work for some inputs (e.g. [1, 2, 3, 4, 5]) 

n = int(input())
t = list(map(int, input().split()))

# sort trees by time required for them to grow
t.sort()

# find the earliest day when the party can be organized
day = 0
for i in range(n):
    if t[i] < day:
        day += 1
    else:
        day += t[i]

print(day)

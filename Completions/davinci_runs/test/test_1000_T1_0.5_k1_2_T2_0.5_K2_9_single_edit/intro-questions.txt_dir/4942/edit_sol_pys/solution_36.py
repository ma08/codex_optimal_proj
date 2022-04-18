

# TODO: fix algorithm - it doesn't work for some inputs (i.e. when the first tree is the tallest)

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
        day = t[i]

print(day)
